# Checagem de conclusão e evidência

Use durante a construção e ao entregar. Marque resultado e evidência por item; não trate esta lista como execução. Leia o preflight do SKILL.md, sem substituir configuração real por texto desta referência.

## Entrada e visual

- Modelo/esforço confirmados: Astra/alto; rápido só se disponível e verificável; alternativa Opus 5.5+ somente conforme catálogo real. Sem confirmação, visual pendente e preparação não visual pode continuar.
- Fonte visual/design system informado reutilizado; se ausente, pergunta inicial curta sem repetição. Fonte inspecionada e versão registrada.
- Tokens semânticos registrados nas categorias disponíveis, com valores/unidades, procedência, oficial/derivado/proposto e aprovação. Inferência de referência não apresentada como token oficial.
- Aprovação explícita da direção representativa ou aprovação reutilizada da mesma versão. Revisão de mudança material delimitada ao afetado.
- Síntese/PRD/SDD/modelo e schema/API/fixtures disponíveis confrontados; lacuna e conflito não tratados como decisão.

## Dados e rastreabilidade

- IDs únicos e canônicos; registros fictícios e relações coerentes; fixture negativa separada da principal.
- Fórmulas e cenários com entradas, limites, resultados esperados, tolerância e tempo pertinentes. Dados/fórmulas divergentes voltam à decisão, não a ajuste silencioso.
- Cada campo possui origem e decisão; derivados têm regra; vínculos semânticos/físicos não são confundidos.
- Ações/eventos, regiões, transições, consultas/operações, dependências e aceite têm referências resolvidas. API proposta e simulação não descritas como implementadas.
- Inventário bidirecional: fluxo/controle obrigatório do contrato tem localização e resultado no protótipo; controle exposto tem origem no contrato. Nenhum obrigatório inerte; destino pendente impede declarar o fluxo pronto.
- Manifesto e contrato não divergem; definições compartilhadas têm uma fonte normativa.

## Interação e estados

- Abertura, edição, salvar/cancelar, validação, feedback, falha/repetição e foco contemplados quando aplicáveis. Último estado válido e entrada recuperável preservados conforme contrato.
- Estados pertinentes com acionamento reproduzível, fixture, mensagem/ação e saída. Quantidade derivada do projeto, sem login/permissões/exclusão inventados.
- Modo de revisão/demonstração separado da operação normal; sair/resetar não corrompe dados válidos nem chama mutação real.
- Com execução disponível: percorrer cenários, recarga/reset, teclado/foco e efeitos cruzados; resultado/captura real por cenário. Não contar apenas nomes de estados.

## Baixa carga cognitiva e inspeção visual

- Instrução e microtexto contêm só o necessário à ação/decisão atual; uma decisão humana por vez, com recomendação e exemplo curto quando necessários.
- Sem avisos repetidos, cartões redundantes, labels técnicos ou instruções concorrentes; detalhes em ajuda contextual ou handoff.
- Erros, obrigatoriedade, consequências relevantes e informação acessível preservados. Não depender só de cor, placeholder ou tooltip para informação essencial.
- Na renderização: referência/tokens, hierarquia, densidade, legibilidade, foco, reflow/contraste e movimento pertinentes inspecionados nas larguras acordadas. Revisão documental não confirma essas propriedades.
- Ferramentas de simulação não competem com a operação normal. Documentação técnica completa permanece no handoff.

## Resultados separados

1. **Revisão documental:** cobertura, fontes, vínculos, conflitos e completude do contrato. Pode ocorrer sem app.
2. **Simulação de contrato:** aplicação explícita das instruções a entradas fictícias; pode calcular expectativas e detectar contradições. Não é app gerado.
3. **Conformidade executada:** fluxos, estados, cálculos, capturas e medições reais do protótipo; não comprova backend.
4. **Aprovação humana:** direção visual e comportamento aprovados explicitamente por versão. Captura ou validador não substituem.

Registre ferramenta/comando quando executado, entrada, saída/resultado, arquivo de evidência e limite do método. Sem ferramenta ou sem execução, use `não executado`, nunca PASS. Ao calibrar um verificador, use caso válido e inválidos significativos (referência órfã, relação rompida, cálculo incompatível, simulação declarada real); teste que apenas busca títulos não comprova contrato nem qualidade visual.

Corrija até três rodadas por tela, com delta. Persistindo falha, liste bloqueio e impacto sem declarar pronto. Entregue fonte/execução local, inventário, contrato versionado, manifesto, tokens, fixtures/expectativas, catálogos e evidências obtidas. Aprovações não são herdadas de outro artefato. Pendência material mantém rascunho; não autoriza backend.
