# Contrato por tela e handoff de implementação

Prepare antes da construção e complete depois com os artefatos reais. O contrato reúne comportamento; o [manifesto](manifesto-tela.md) fornece vínculos estruturados. Referencie definições compartilhadas por ID, sem duplicação normativa. Agrupe blocos quando isso tornar a leitura mais clara; não há quota de seções.

## Identidade, fontes e cobertura

ID, versão, tarefa, rota/localização, status, fontes e decisões aprovadas. Inclua síntese/PRD/SDD, modelo/dicionário/schema/API e referência visual conforme disponíveis. Liste cobertura, conflitos materiais e lacunas. Registre caminho real da fonte e capturas existentes; antes de produzir use `não produzido`. Separe aprovação visual e de comportamento, com evidência da versão ou pendência.

## Visual e informação essencial

Referencie registro de tokens/componentes e direção visual aprovada; liste extensões propostas. Registre por tarefa a ação principal, o que o usuário precisa saber agora e o que foi movido para ajuda/handoff. Não despeje documentação técnica na interface. Erro, obrigatoriedade, consequência relevante e acessibilidade não podem desaparecer para reduzir texto.

## Campos e dados

Para cada campo/valor: ID canônico, rótulo, origem `persistido/derivado/visual/proposto`, situação da decisão, vínculo semântico/físico, regiões, uso, formato, limites/defaults conhecidos e fonte. Derivados apontam para regra/fórmula e entradas. Campos ocultos/preenchidos por serviço são registrados quando sustentados. Relações trazem sentido, cardinalidade confirmada ou lacuna e efeito na tarefa.

## Catálogo de ações, eventos e navegação

Por ação: ID, gatilho/evento, entrada, pré-condições, validação, abertura/edição/confirmação/cancelamento aplicáveis, modalidade, resultado, mensagem, transição, próxima rota, dados preservados, foco e recuperação. Registre retorno visual e último estado válido após falha. Diferencie medição e edição estrutural somente quando o domínio exigir. Efeitos cruzados e propriedade de um dado atualizado em mais de uma tela precisam ficar claros.

Eventos têm emissor, momento, payload conhecido e efeito/consumidor pertinente. Não invente infraestrutura de eventos. Confirme destinos e dependências; ação obrigatória sem destino funcional é pendência impeditiva para a tarefa.

## Operações, modelo e API

Ligue campos e ações a conceitos/schema e consultas/operações. Reutilize contrato API existente; registre sua versão e verificação documental ou executada. Endpoints ainda não existentes são propostas, sem alegar implementação. Atomicidade, concorrência e autoridade futura do backend só entram quando sustentadas ou como pendência material; não implemente backend aqui.

## Regras, fórmulas e mensagens

Regras têm ID, fonte e estado de decisão. Fórmulas têm entradas canônicas, limites, unidade, arredondamento/tolerância e data de referência quando pertinentes. Não preencha lacuna de regra com decisão técnica silenciosa.

Catálogo de mensagens: ID, condição, texto essencial exato quando conhecido, campo/ação/estado associado e origem. Texto novo é proposta até aprovação. Mensagem de erro oferece recuperação, sem expor termos técnicos desnecessários. Retornos extensos ficam em ajuda contextual se não forem essenciais à ação.

## Matriz de estados e interações

Referencie a matriz de [fixtures e estados](fixtures-interacoes-estados.md): estados pertinentes, forma reproduzível de alcançar cada um, representação/mensagem, ações e saída, dados/foco preservados, fixture e evidência. Operação normal e modo de revisão são separados. Não invente login, permissão, exclusão ou número fixo de estados. Estado escrito não conta como testado.

## Fixtures, armazenamento e exemplos calculáveis

Fonte/versão do conjunto fictício, IDs/relações, cenários principal/vazio/limites/erros aplicáveis, resultados esperados e reset. Registre memória/armazenamento do navegador, recarga/reinício e fronteira da simulação. Não use dados pessoais reais nem invente histórico como fato. Amostra negativa é isolada do conjunto válido.

## Cenários e critérios de aceite

| ID | Fontes/regras/estados | Dados/fixture | Dado/Quando/Então observável | Modalidade | Resultado/evidência |
| --- | --- | --- | --- | --- | --- |

Exija um resultado observável para cada regra/estado relevante e controle obrigatório. Modalidade: documental, simulação de contrato, conformidade de protótipo executada ou contrato futuro de backend. Resultado: `não executado`, `passou`, `falhou` ou `bloqueado`. Não atribua PASS de aplicativo a um cálculo ou cenário apenas descrito.

## Handoff, conflitos e continuidade

Mantenha índice com telas/fluxos e referências aos catálogos de ações/eventos, mensagens, tokens, fixtures/fórmulas, API/modelo, dependências, simulado versus real, conflitos/propostas/pendências e evidências. Conteúdo compartilhado fica em uma fonte, referenciada por tela. Mudanças registram versão, impacto e quais verificações/aprovações precisam ser refeitas. O índice não substitui contrato individual.

Pronto requer controles/fluxos e estados executados e revisão visual real quando o pedido inclui protótipo funcional. Sem execução/captura ou com pendência material, entregue rascunho e limites. Handoff não autoriza automaticamente implementar backend.
