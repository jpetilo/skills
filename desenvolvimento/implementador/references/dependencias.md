# Motor, preflight e compatibilidade

Dependência instalada, não embutida: `DEPENDENCIA_LOCAL`. Preservar seus originais. A autoria local do plugin é Jefferson; licença não identificada nos arquivos inspecionados. Esta entrada é autoral e fina, não uma cópia do motor.

Fontes reais:

- orquestrar-roadmap (dependência local; consultar `DEPENDENCIAS.md` na raiz) e controlador (dependência local; consultar `DEPENDENCIAS.md` na raiz).
- gerar-roadmap (dependência local; consultar `DEPENDENCIAS.md` na raiz): ponte M1→M2 e compilação determinística.
- checkpoint-onda.py (dependência local; consultar `DEPENDENCIAS.md` na raiz): roadmap e test-contract são entradas reais, não criadas por este wrapper.

Foram encontrados somente os perfis `next16-supabase`, `web-app-supabase` e `expo-supabase` na pasta process-profiles desta versão. O primeiro inclui Supabase Auth e contexto de tenant; os demais também são específicos de Supabase. Não foi encontrado perfil SQLite local sem login. Não afirmar compatibilidade executável com esse cenário só porque o motor de orquestração é genérico.

O novo PRD/SDD inicial e o handoff do Prototipador não geram, por si, `phase-1-exit.yaml`, `prototype-screen-contracts.yaml`, núcleos/casos de uso, roadmap ou test-contract nativos. Essa conciliação e o perfil compatível são dependências explícitas antes da execução; não foram implementados nesta preparação. Escolher ou criar um perfil exige escopo próprio, sem mudar a decisão de produto para encaixar o perfil.

O motor lê o menor número de onda ainda incompleta e as dependências de cada item. Não existe uma opção nativa `--onda-unica` na interface inspecionada. Não confundir uma fatia compacta com ignorar integração, revisões ou qualidade final.

Se o plugin mudar de versão/local, confira novamente os caminhos e contratos antes de usar. Não copiar só um script para fazê-lo parecer independente das demais dependências.
