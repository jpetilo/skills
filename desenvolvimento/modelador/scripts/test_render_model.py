"""Regression tests for semantic safeguards and offline output, without packages."""
import copy
import json
from pathlib import Path
import runpy
import unittest
import xml.etree.ElementTree as ET

api=runpy.run_path(str(Path(__file__).with_name('render_model.py')))

def fixture():
    return {'title':'Teste <seguro>','subtitle':'','layer':'conceitual','width':800,'height':600,'sources':{'D1':'Fonte de teste'},'nodes':[
        {'id':'A','label':'Origem <script>','lines':[],'status':'decidido','sources':['D1'],'x':40,'y':170,'w':220,'h':100},
        {'id':'B','label':'Destino','lines':[],'status':'proposto','sources':['D1'],'x':500,'y':170,'w':220,'h':100}],
        'edges':[{'id':'R1','from':'A','to':'B','label':'relaciona','status':'decidido','sources':['D1'],'target_per_source':'0..N','source_per_target':'1','identifying':False,'points':[[260,220],[500,220]],'label_at':[380,320]}],'notes':[]}

class RenderTests(unittest.TestCase):
    def test_complete_er_direction_and_identification(self):
        model=fixture();api['validate'](model)
        self.assertIn('A ||..o{ B',api['mermaid'](model))
        model['edges'][0]['identifying']=True
        self.assertIn('A ||--o{ B',api['mermaid'](model))

    def test_unknown_information_is_not_invented(self):
        for field,value in [('target_per_source','?'),('identifying',None)]:
            with self.subTest(field=field):
                model=fixture();model['edges'][0][field]=value
                api['validate'](model)
                output=api['mermaid'](model)
                self.assertTrue(output.startswith('flowchart'))
                self.assertNotIn('||..o{',output)

    def test_invalid_structure_is_rejected(self):
        changes=[lambda m:m['nodes'].append(copy.deepcopy(m['nodes'][0])),
                 lambda m:m['edges'][0].update(to='UNKNOWN'),
                 lambda m:m['edges'][0].update(target_per_source='NN'),
                 lambda m:m['nodes'][0].update(sources=['NO_SOURCE']),
                 lambda m:m['nodes'][1].update(x=60),
                 lambda m:m['edges'][0].update(points=[[260,220],[801,220]])]
        for change in changes:
            with self.subTest(change=change):
                model=fixture();change(model)
                with self.assertRaises(ValueError):api['validate'](model)

    def test_editable_er_preserves_attributes_and_keys(self):
        model=fixture()
        model['nodes'][0]['canonical_name']='origem'
        model['nodes'][1]['canonical_name']='destino'
        model['nodes'][0]['attributes']=[{'name':'origem_id','type':'identifier','keys':['PK'],'status':'proposto','sources':['D1'],'comment':'Chave lógica'}]
        api['validate'](model)
        self.assertIn('identifier origem_id PK',api['mermaid'](model))
        self.assertIn('origem ||..o{ destino',api['mermaid'](model))
        self.assertIn('[proposto]',api['mermaid'](model))

    def test_invalid_or_untraced_attributes_are_rejected(self):
        base={'name':'origem_id','type':'identifier','keys':['PK'],'status':'proposto','sources':['D1']}
        for change in [{'keys':['NN']},{'name':'idOrigem'},{'sources':['UNKNOWN']},{'type':'integer;DROP'}]:
            with self.subTest(change=change):
                model=fixture();attribute=dict(base);attribute.update(change)
                model['nodes'][0]['attributes']=[attribute]
                with self.assertRaises(ValueError):api['validate'](model)

    def test_svg_is_well_formed_and_escapes_untrusted_labels(self):
        model=api['validate'](fixture())
        rendered=api['svg'](api['make_scene'](model))
        root=ET.fromstring(rendered)
        self.assertEqual(root.tag,'{http://www.w3.org/2000/svg}svg')
        self.assertIn('&lt;script&gt;',rendered)
        self.assertNotIn('<script>',rendered)
        self.assertFalse(root.findall('.//{http://www.w3.org/2000/svg}script'))

if __name__=='__main__':unittest.main()
