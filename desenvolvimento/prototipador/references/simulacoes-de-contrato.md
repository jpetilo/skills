# Avaliação por simulação de contrato

Estas são entradas sintéticas autocontidas para avaliar instruções da skill, sem ler ou alterar projetos de produto. Não são requisitos universais, geração de protótipo, inspeção de imagem ou teste de aplicativo.

Leia apenas ao avaliar uma mudança da skill. Dados e expectativas estão em [simulacoes.fixture.json](simulacoes.fixture.json). O script [verificar_exemplos.py](../scripts/verificar_exemplos.py) usa somente biblioteca padrão para conferir cálculos, integridade e rejeição de exemplos corrompidos. Ele não valida visual, acessibilidade, cobertura de manifesto arbitrário ou comportamento do agente.

## Simulação 1: medição de objetivos

**Pedido sintético:** "Com os requisitos e schema fornecidos, prototipe consultar um objetivo e alterar apenas a medição de seus resultados. Reutilize o arquivo de tokens informado. Sem login ou exclusão."

**Entrada explícita:** regras e entidades do caso `okr` da fixture. Neste teste, um arquivo de tokens fictício é informado como fonte: texto/superfície/ação, família e entrelinha, espaçamento e foco estão declarados; movimento/elevação não estão. Não é um design system real inspecionado. Os nomes físicos indicados em `acao.campo` são fornecidos pela entrada sintética, não inferidos do projeto OKR.

**Aplicação documental das instruções:**

| Decisão | Resposta simulada do executor |
| --- | --- |
| Abertura | Reutilizar tokens já informados; não perguntar design system novamente. Registrar tokens declarados como oficiais da fonte sintética, nunca de uma marca real. |
| Lacunas visuais | Movimento e elevação ficam pendentes ou propostas motivadas; não alegar extração. Sem renderização, direção/aprovação visual não comprovadas. |
| Superfície | Consulta e medição; nenhum CRUD extra. Distinguir medição de edição estrutural porque esta entrada explicitamente o exige. |
| Dados | IDs empresa/objetivo/KR coerentes. Objetivo de equipe alinhado não altera a média empresarial. |
| Interação | Abrir e focar medição; editar rascunho; salvar confirma; cancelar preserva 40; entrada inválida preserva último confirmado e mostra erro essencial no campo. |
| Expectativas | KR-A 25% e KR-B 40% dão 32,5%; confirmar 60 torna KR-A 50% e objetivo 45%; empresarial segue 80%. Valor 120 dá contribuição limitada em 100%, sem assumir limite físico adicional. |
| Estados | Principal, carregando simulado, vazio do recorte, inválido, falha e sucesso se pertinentes; acionamentos ficam no modo de revisão, sem barra técnica no fluxo de medição. |
| API/rastreabilidade | OP-MEDIR proposta, endpoint pendente; não chamar backend. Campo físico conhecido e cálculo derivado rastreados separadamente. |
| Carga cognitiva | Rótulo de medição, valor e salvar/cancelar; fórmula/contexto técnico no handoff. Erro e unidade essenciais permanecem visíveis. |
| Conflito deliberado | Se outra fonte disser rollup empresarial, registrar conflito e perguntar essa decisão antes de implementar; não ajustar fixture/regra silenciosamente. |
| Evidência | Resultado desta simulação é documental. Valores são conferidos pelo script de exemplos; nenhum controle ou captura foi executado. |

## Simulação 2: reserva em biblioteca

**Pedido sintético:** "Mostre livros e simule reservar exemplares disponíveis. Sem login e sem exclusão. Não tenho tokens; quero partir de uma referência visual."

**Entrada explícita:** caso `biblioteca`, modelo semântico sem schema físico e sem API existente. Nenhum link/arquivo visual foi efetivamente recebido nesta simulação; não há imagem a inspecionar.

| Decisão | Resposta simulada do executor |
| --- | --- |
| Primeira pergunta | "Qual referência visual devo usar? Pode enviar um link ou arquivo." É a única decisão visual pendente agora; não repetir pergunta sobre tokens já respondida. |
| Trabalho independente | Preparar catálogo, fixtures, matriz e contrato enquanto aguarda referência. Sem paleta/fonte inventadas e sem declarar direção aprovada. Depois de inspecionar referência real, propor tokens mínimos como inferências e validar a direção. |
| Modelo | LIV-A tem 3 exemplares e empréstimo fictício de 2; saldo calculado 1. Reserva.quantidade é ID semântico; tabela/coluna física permanecem pendentes. |
| Interação | Rascunho 1 não altera saldo; cancelar preserva 1; confirmar 1 simula saldo 0. Solicitar 2 é inválido e preserva saldo 1, com mensagem proposta "Há 1 exemplar disponível." |
| Estados | Com livros, busca sem resultado, coleção vazia e inválido/sucesso aplicáveis. Não criar login, permissão ou exclusão. Revisão separada permite reproduzir cenário vazio sem apagar livros. |
| API/evento | OP-RESERVAR é proposta sem endpoint. Evento de confirmação é evento de interface; não alegar fila/barramento implementado. |
| Carga cognitiva | Quantidade, disponibilidade e ação principal bastam; fórmulas/IDs no handoff. Cancelamento/falha preservam entrada pertinente e foco. |
| Limite | Pré-condição de modelo para criação visual continua aplicável; esta simulação não fornece evidência de modelo efetivo nem cria design. |

## Avaliação e limites

As duas simulações exercitam decisões diferentes: tokens já informados versus referência ausente, schema conhecido versus modelo semântico, cálculo percentual versus contagem inteira, distinção de medição pertinente versus reserva simples. As decisões acima foram conferidas por leitura das novas instruções; não houve execução de agente independente ou navegador.

O script executa as expectativas numéricas/relacionais e casos negativos: ID duplicado, vínculo órfão, operação sem dono, simulação apresentada como real, meta inválida e reserva excedente. Seu PASS significa somente que esses exemplos e suas rejeições passaram. O validador oficial de skills confere frontmatter/nome; não comprova eficácia visual.

Registre o resultado real da execução em `avaliacao-20261021.md`. Não converta a simulação em evidência de produto, nem use estes domínios ou quantidades como padrão de novas tarefas.
