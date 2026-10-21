"""Own offline model renderer. Standard-library SVG; optional Windows GDI PNG."""
import argparse
import html
import json
import math
import os
from pathlib import Path
import re
import subprocess

STATUSES = {'decidido', 'proposto', 'hipótese', 'pendente'}
CARDS = {'1', '0..1', '0..N', '1..N', '?'}
COLORS = {'decidido': '#175a79', 'proposto': '#936015', 'hipótese': '#76548b', 'pendente': '#9a443f'}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def validate(model):
    require(model.get('layer') in {'conceitual', 'logico', 'fisico'}, 'Invalid model layer')
    w, h = model['width'], model['height']
    require(all(isinstance(v, (int, float)) and math.isfinite(v) and 200 <= v <= 10000 for v in (w, h)), 'Invalid canvas')
    sources = model.get('sources', {})
    require(isinstance(sources, dict) and sources, 'Sources required')
    ids = set()
    boxes = []
    canonical_names=set()
    for node in model['nodes']:
        require(re.fullmatch(r'[A-Z][A-Z0-9_]*', node['id']) and node['id'] not in ids, 'Invalid/duplicate entity ID')
        ids.add(node['id'])
        if 'canonical_name' in node:
            require(re.fullmatch(r'[a-z][a-z0-9_]*',node['canonical_name']) and node['canonical_name'] not in canonical_names, 'Invalid/duplicate canonical name')
            canonical_names.add(node['canonical_name'])
        attributes=node.get('attributes', [])
        require(isinstance(attributes,list), 'Attributes must be a list')
        attribute_names=set()
        for attribute in attributes:
            name=attribute.get('name','')
            require(re.fullmatch(r'[a-z][a-z0-9_]*',name) and name not in attribute_names, 'Invalid/duplicate attribute name')
            attribute_names.add(name)
            require(re.fullmatch(r'[a-z][a-z0-9_]*',attribute.get('type','')), 'Invalid semantic attribute type')
            keys=attribute.get('keys',[])
            require(isinstance(keys,list) and len(set(keys))==len(keys) and set(keys)<={'PK','FK','UK'}, 'Invalid attribute keys')
            require(attribute.get('sources') and all(ref in sources for ref in attribute['sources']), 'Attribute source missing')
            require(attribute.get('status') in STATUSES, 'Invalid attribute status')
        x,y,bw,bh = (node[k] for k in ('x','y','w','h'))
        require(all(isinstance(v,(int,float)) and math.isfinite(v) for v in (x,y,bw,bh)), 'Invalid geometry')
        require(0 <= x < x+bw <= w and 0 <= y < y+bh <= h and bw >= 100 and bh >= 60, 'Entity outside canvas')
        require(node['status'] in STATUSES, 'Invalid entity status')
        require(node.get('sources') and all(s in sources for s in node['sources']), 'Entity source missing')
        require(isinstance(node.get('lines', []), list), 'Entity lines must be a list')
        require(67 + len(node.get('lines', []))*24 <= bh, 'Entity text exceeds box height')
        for ox,oy,ow,oh in boxes:
            require(x+bw <= ox or ox+ow <= x or y+bh <= oy or oy+oh <= y, 'Overlapping entity boxes')
        boxes.append((x,y,bw,bh))
    edge_ids = set()
    for edge in model['edges']:
        require(re.fullmatch(r'[A-Z][A-Z0-9_]*',edge['id']) and edge['id'] not in edge_ids, 'Invalid/duplicate relation ID')
        edge_ids.add(edge['id'])
        require(edge['from'] in ids and edge['to'] in ids, 'Orphan relation endpoint')
        require(edge['status'] in STATUSES, 'Invalid relation status')
        require(edge.get('sources') and all(s in sources for s in edge['sources']), 'Relation source missing')
        require(edge['target_per_source'] in CARDS and edge['source_per_target'] in CARDS, 'Invalid cardinality')
        require(edge.get('identifying') is None or type(edge['identifying']) is bool, 'Invalid identification qualifier')
        require(len(edge['points']) >= 2, 'Relation needs a path')
        for point in [*edge['points'], edge['label_at']]:
            require(len(point) == 2 and all(isinstance(v,(int,float)) and math.isfinite(v) for v in point), 'Invalid relation point')
            require(0 <= point[0] <= w and 0 <= point[1] <= h, 'Relation outside canvas')
    return model

def text(scene, value, x, y, size=18, color='#183543', bold=False, align='left', background=False):
    scene.append({'type':'text','text':str(value),'x':x,'y':y,'size':size,'color':color,'bold':bold,'align':align,'background':background})

def make_scene(model):
    scene=[]
    text(scene,model['title'],40,30,30,bold=True)
    text(scene,model.get('subtitle',''),40,78,18)
    text(scene,'Conceitos e relações para revisão · ? = cardinalidade não confirmada',40,110,17)
    for edge in model['edges']:
        scene.append({'type':'line','points':edge['points'],'color':COLORS[edge['status']],'width':2})
    for node in model['nodes']:
        scene.append({'type':'rect','x':node['x'],'y':node['y'],'w':node['w'],'h':node['h'],'fill':'#f5f8fa','stroke':COLORS[node['status']]})
        text(scene,node['label'],node['x']+15,node['y']+14,22,bold=True)
        text(scene,node['status']+' · '+', '.join(node['sources']),node['x']+15,node['y']+46,14,COLORS[node['status']])
        for i,line in enumerate(node.get('lines',[])):
            text(scene,line,node['x']+15,node['y']+74+i*24,17)
    for edge in model['edges']:
        x,y=edge['label_at']
        labels=[edge['label'],edge['from']+'→'+edge['to']+': '+edge['target_per_source']+' | inversa: '+edge['source_per_target'],edge['status']+' · '+', '.join(edge['sources'])]
        for i,label in enumerate(labels):
            text(scene,label,x,y+i*21,15,COLORS[edge['status']],align='center',background=True)
    start=model['height']-40-len(model.get('notes',[]))*25
    for i,note in enumerate(model.get('notes',[])):
        text(scene,note,40,start+i*25,17)
    return {'width':model['width'],'height':model['height'],'items':scene}

def svg(scene):
    esc=lambda value:html.escape(str(value),quote=True)
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{scene["width"]}" height="{scene["height"]}" viewBox="0 0 {scene["width"]} {scene["height"]}" role="img" aria-labelledby="title desc">', '<title id="title">Modelo de domínio para revisão</title><desc id="desc">Conceitos e relações com status, fontes e cardinalidades; interrogação indica informação não confirmada.</desc>', '<rect width="100%" height="100%" fill="#ffffff"/>']
    for item in scene['items']:
        if item['type']=='rect':
            out.append(f'<rect x="{item["x"]}" y="{item["y"]}" width="{item["w"]}" height="{item["h"]}" rx="6" fill="{item["fill"]}" stroke="{item["stroke"]}" stroke-width="2"/>')
        elif item['type']=='line':
            points=' '.join(f'{x},{y}' for x,y in item['points'])
            out.append(f'<polyline points="{points}" fill="none" stroke="{item["color"]}" stroke-width="{item["width"]}"/>')
        else:
            anchor='middle' if item['align']=='center' else 'start'
            style='paint-order:stroke;stroke:#fff;stroke-width:7px;stroke-linejoin:round;' if item['background'] else ''
            weight='600' if item['bold'] else '400'
            out.append(f'<text x="{item["x"]}" y="{item["y"]+item["size"]}" text-anchor="{anchor}" font-family="Segoe UI,Arial,sans-serif" font-size="{item["size"]}" font-weight="{weight}" fill="{item["color"]}" style="{style}">{esc(item["text"])}</text>')
    return '\n'.join(out+['</svg>'])+'\n'

def mermaid(model):
    # Preserve missing information instead of inventing ER qualifiers.
    complete=all(e['target_per_source']!='?' and e['source_per_target']!='?' and type(e.get('identifying')) is bool for e in model['edges'])
    if complete:
        left={'1':'||','0..1':'|o','0..N':'}o','1..N':'}|'}
        right={'1':'||','0..1':'o|','0..N':'o{','1..N':'|{'}
        entity_names={node['id']:node.get('canonical_name',node['id']) for node in model['nodes']}
        result=['erDiagram']
        for node in model['nodes']:
            if not node.get('attributes'):
                result.append(f'    {entity_names[node["id"]]}')
                continue
            result.append(f'    {entity_names[node["id"]]} {{')
            for attribute in node['attributes']:
                keys=', '.join(attribute.get('keys',[]))
                qualifier=(' '+keys) if keys else ''
                comment=(attribute.get('comment','')+' ['+attribute['status']+']').replace('"',"'").replace('\n',' ')
                result.append(f'        {attribute["type"]} {attribute["name"]}{qualifier} "{comment}"')
            result.append('    }')
        for e in model['edges']:
            label=e['label'].replace('"',"'").replace('\n',' ')
            line='--' if e['identifying'] else '..'
            result.append(f'    {entity_names[e["from"]]} {left[e["source_per_target"]]}{line}{right[e["target_per_source"]]} {entity_names[e["to"]]} : "{label} [{e["status"]}]"')
    else:
        result=['flowchart LR','    %% Visão conceitual: qualificadores ER incompletos; não é ER Mermaid completo.']
        def safe(value):
            return html.escape(str(value),quote=True).replace('\n',' ')
        result += [f'    {n["id"]}["{safe(n["label"])}"]' for n in model['nodes']]
        for e in model['edges']:
            label=safe(e['label']+'; '+e['from']+'→'+e['to']+': '+e['target_per_source']+'; inversa: '+e['source_per_target']+'; '+e['status'])
            result.append(f'    {e["from"]} ---|"{label}"| {e["to"]}')
    return '\n'.join(result)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model',type=Path)
    parser.add_argument('--output',required=True,type=Path,help='Authorized output prefix')
    parser.add_argument('--png',action='store_true')
    parser.add_argument('--overwrite',action='store_true')
    args=parser.parse_args()
    model=validate(json.loads(args.model.read_text(encoding='utf-8-sig')))
    scene=make_scene(model)
    paths=[args.output.with_suffix(s) for s in ['.svg','.mmd','.scene.json']]
    if args.png:
        paths.append(args.output.with_suffix('.png'))
    require(args.overwrite or not any(p.exists() for p in paths),'Output exists; use a new prefix or --overwrite')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    paths[0].write_text(svg(scene),encoding='utf-8')
    paths[1].write_text(mermaid(model),encoding='utf-8')
    paths[2].write_text(json.dumps(scene,ensure_ascii=False,indent=2),encoding='utf-8')
    if args.png:
        require(os.name=='nt','PNG fallback requires Windows/System.Drawing; SVG was generated')
        command=['powershell.exe','-NoProfile','-File',str(Path(__file__).with_name('render_scene.ps1')),'-Scene',str(paths[2].resolve()),'-Output',str(paths[3].resolve())]
        subprocess.run(command,check=True)
    for p in paths:
        print(p.resolve())

if __name__=='__main__':
    main()
