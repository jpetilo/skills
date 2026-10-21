---
name: prototipador
description: "Crie ou revise protótipos ricos navegáveis e handoffs por tela a partir de síntese validada, PRD/SDD, modelo de dados e design system ou referência visual. Inclui fixtures fictícias coerentes, estados reproduzíveis, baixa carga cognitiva e rastreabilidade para implementação posterior. Não cria backend, migrations ou deploy."
metadata:
  version: "1.1.0"
---

# Prototipador

Produza uma experiência navegável e um contrato que permita implementá-la sem adivinhar. A base combina Protótipo Rico do Agentic Builder e E3/E4 do CFS; as [origens](references/origens.md) delimitam a adaptação. Domínio, ferramenta, marca e estrutura de saída vêm do projeto, não dos exemplos da skill.

## 0. Preflight do modelo para criação visual

Preferência exigida pelo usuário: **Astra com esforço alto e modo rápido quando disponível**. Alternativa autorizada: **Opus 5.5 ou superior**, somente se essa versão existir no catálogo real do executor. Não inventar IDs, versões ou disponibilidade. "Alto rápido" não significa "Auto"; não exigir modo Auto nem mapear o pedido para ele.

Antes de criar ou alterar design/protótipo visual:

- Consultar a configuração efetiva por orquestrador/ferramenta disponível e registrar modelo, esforço, origem da evidência e, separadamente, disponibilidade/estado do modo rápido. Um catálogo comprova opções disponíveis, não qual modelo executa o turno atual. Texto desta skill não troca o próprio modelo.
- Resolver o identificador real de Astra no executor e selecionar esforço alto quando suportado/autorizado. Usar Opus 5.5+ como alternativa somente com catálogo e configuração verificáveis; informar a seleção real, sem fallback silencioso para outro modelo.
- Ativar modo rápido somente se houver controle real disponível. Se a API expõe apenas `model`/`thinking`, registrar que a velocidade não pode ser configurada ou confirmada por esse canal; não inventar parâmetro `service_tier` nem afirmar modo rápido ligado. Essa limitação, sozinha, não bloqueia uma execução confirmada em Astra/alto.
- Se a seleção exigida não for suportada ou o modelo/esforço ativo não puder ser confirmado, avisar antes de gerar design e bloquear **somente a criação visual** até decisão/encaminhamento do orquestrador. Continuar leitura, manutenção e preparação não visual pertinentes. Não produzir um design paralelo em outro modelo.

Aplicar este preflight também ao retomar uma etapa em novo turno/executor. A autorização para prototipar não dispensa a preferência explícita de modelo. A [checagem](references/checagem-handoff.md) registra a condição real, sem prometer qualidade apenas pelo nome do modelo.

## 1. Confira fontes, destino e design system

Leia as versões pertinentes da síntese validada do Investigador, PRD, SDD, modelo/dicionário e, quando disponíveis, schema/DDL, contrato API e fixtures. Registre origem, cobertura, aprovação e lacunas. Síntese pode sustentar um recorte parcial identificado; não a renomeie como documentação completa. Modelo conceitual não prova colunas físicas nem banco executado. A disponibilidade de API documentada não prova operação real.

Reutilize o design system já informado. Se não houver design system, tokens, biblioteca ou referência visual na conversa/arquivos pertinentes, pergunte ao iniciar: **"Qual design system devo usar? Envie um link, tokens, biblioteca ou referência visual."** Não repita pergunta respondida. Se o usuário não possuir nenhum, ofereça uma direção mínima como proposta. Prepare dados e contratos enquanto resolve essa decisão; não declare direção visual aprovada por silêncio.

Leia [design e carga cognitiva](references/design-e-carga-cognitiva.md) para inspecionar a fonte e registrar tokens semânticos de cores, tipografia, espaçamento, raios, foco, elevação e movimento conforme disponíveis. Diferencie oficiais, derivados e propostas, com procedência. URL inacessível é lacuna, não licença para imaginar a referência.

Preserve `decidido`, `proposto`, `hipótese` e `pendente`. Conflito material entre fontes deve ser localizado e levado à decisão; não implemente silenciosamente uma regra divergente. Consulte respostas e decisões já existentes antes de perguntar. Resolva o destino antes de escrever; artefatos do produto não vão para a pasta da skill. Em modo documental, prepare contratos sem gerar app, telas executáveis ou banco.

## 2. Baixa carga cognitiva obrigatória

Toda instrução ao usuário e todo microtexto da interface deve conter **apenas o essencial para a decisão ou ação atual**. Quando precisar de decisão humana, apresente uma por vez, com exemplo curto e recomendação clara. Não transforme isso em um quiz fixo nem peça confirmação de mero andamento.

Evite parágrafos repetidos, avisos permanentes desnecessários, excesso de cartões, labels técnicos e instruções concorrentes. Use ajuda contextual ou divulgação progressiva para detalhes; reserve o handoff para a documentação técnica completa. Não esconda erros, campos obrigatórios, consequências relevantes, rótulos acessíveis ou informação necessária à tarefa. Brevidade não autoriza omissão.

Ferramentas para simular estados ficam em **modo separado de revisão/demonstração**, identificado e reversível, sem ocupar o fluxo normal. Sinalize simulação onde ela altera a interpretação da ação, sem repetir o mesmo aviso em cada bloco. Revise essa regra na composição real de cada tela, não apenas no texto do contrato.

## 3. Planeje jornadas, fixtures e estados

Derive um inventário de fluxos/tarefas e telas do escopo. Não transforme toda entidade em tela nem acrescente CRUD, login, permissões, exclusão ou multitenancy por rotina. Identifique ações necessárias, controles, dados, regras e resultado observável antes de construir.

Leia [fixtures, interações e estados](references/fixtures-interacoes-estados.md). Reutilize fixtures fictícias autorizadas ou derive exemplos da síntese/PRD/SDD/modelagem, com IDs canônicos, relações íntegras e resultados calculáveis. Cubra principal, vazio, limites e erros aplicáveis; propostas de amostra não viram requisitos. Não use dados pessoais reais nem apresente histórico inventado como fato.

Prepare por tela uma matriz de estados pertinentes com cenário, acionamento reproduzível, mensagem, ação disponível, saída e preservação dos dados. A quantidade vem do projeto, sem quota fixa. Planeje abertura, edição, salvar, cancelar, foco, validação, retorno visual e falha para cada ação aplicável. Distinga medição e edição estrutural somente se as regras do domínio exigirem.

## 4. Aprove a direção e construa

Renderize um modelo visual representativo antes de multiplicar telas. Se houver ambiguidade material, compare alternativas renderizadas com uma recomendação. Reutilize aprovação explícita da mesma versão ou obtenha a validação da direção proposta; referência fornecida não aprova automaticamente as decisões derivadas. Mudança material invalida apenas verificações/aprovações afetadas.

Use frontend, biblioteca e caminhos acordados. Na continuidade do projeto, preserve os arquivos definitivos em vez de duplicar a experiência. Não imponha Agentic, CFML, Claude Design, dois quadros ou sintaxe de uma ferramenta a todo projeto. Adapte formato e nomes quando o usuário escolher a ferramenta.

Implemente navegação, interações e estados contratados. Para cada ação declare `simulada`, `real existente` ou `pendente`. Memória ou armazenamento do navegador podem simular persistência; registre comportamento ao recarregar, reiniciar e resetar. Nunca conte isso como persistência real do backend.

Não crie endpoints, autenticação real, transações de backend, migrations, seeds executados, integrações ou deploy. Uma operação real existente só pode ser usada com autorização e alvo confirmado. A escolha de tecnologia informa o contrato, não autoriza execução externa.

## 5. Mantenha manifesto e contrato por tela

Leia [contrato por tela](references/contrato-tela.md) antes da construção e complete-o com caminhos e evidências reais depois. Use o [manifesto rastreável](references/manifesto-tela.md) para registrar campos canônicos, origem persistido/derivado/visual/proposto, regiões, ações/eventos, estados, transições, regras, dependências, consultas/operações e aceite.

Schema e API existentes informam vínculos; operação ainda não existente permanece proposta ou pendência. Use `data-regiao`, `data-acao`, `data-campo`, `data-estado` ou equivalente rastreável. `tabela.coluna` só quando conhecido; caso contrário, ID semântico e vínculo físico pendente. Não exija `x-dc`, `sc-for` ou `renderVals` fora da ferramenta correspondente.

Ligue regra, fórmula, estado e mensagem a cenário observável, preferencialmente Dado/Quando/Então. Texto novo é proposta; mensagem essencial deve ser curta e ter condição precisa. Preserve conflitos, propostas e pendências. Não esconda regra em código nem repita cópias normativas da mesma decisão entre manifesto e contrato.

## 6. Verifique, corrija e entregue

Use a [checagem de conclusão](references/checagem-handoff.md). Confronte fluxos planejados e controles com o protótipo: nenhum controle obrigatório pode ficar inerte ou apontar para destino inexistente. Controles pendentes impedem declarar a respectiva tarefa pronta. Estados devem ser acionáveis; fixtures e cálculos consistentes; direção visual e baixa carga cognitiva revisadas.

Com execução/captura disponíveis, percorra fluxos, teclado, foco, edição/cancelamento, falhas e estados; renderize nas larguras pertinentes e inspecione o resultado. Guarde capturas e resultados reais por cenário. Se não puder executar, registre `não executado` e o motivo; checklist documental não comprova visual, interação ou backend.

Corrija até três rodadas por tela, registrando o delta. Se persistirem falhas, entregue bloqueios e impacto sem declarar pronto. Decisão de domínio volta à fonte; não a resolva como ajuste cosmético.

Entregue fonte e execução local, inventário de fluxos/telas, manifesto, contrato individual versionado, registro de tokens, fixtures e resultados esperados, catálogos de ações/eventos e mensagens, ligações API/modelo e evidências obtidas. O índice pode apontar para definições compartilhadas, sem repetir mecanicamente seções por tela. Handoff técnico completo fica fora do fluxo normal do usuário.

Separe **revisão documental, conformidade executada, aprovação visual e aprovação de comportamento**. O pacote nasce `rascunho`; só registre aprovação explícita da versão apresentada. Pendências materiais impedem alegar contrato fechado. Esta entrega não implementa nem autoriza backend.

Para avaliar mudanças nesta própria skill sem criar app, use as [simulações de contrato](references/simulacoes-de-contrato.md); elas não são evidência de um protótipo gerado ou visualmente aprovado.
