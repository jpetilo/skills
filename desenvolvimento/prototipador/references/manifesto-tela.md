# Manifesto rastreável por tela

Use JSON ou formato estruturado equivalente já adotado. O manifesto deve permitir conferir relações, não apenas listar títulos. Defina dados normativos uma vez e referencie-os por ID no contrato e no índice.

## Estrutura mínima adaptável

| Coleção/campo | Conteúdo requerido quando aplicável |
| --- | --- |
| Tela | ID, versão, tarefa, rota/local, caminho real da fonte, status e referências de origem/versionamento. |
| Fontes | IDs de síntese/PRD/SDD/modelo/dicionário/schema/API/referência visual e cobertura. Ausentes são pendências, não caminhos fabricados. |
| Regiões | ID, função, campos/ações/estados que apresentam. |
| Campos | ID canônico, rótulo, tipo de origem, referência semântica/física, regiões, uso/formato/limites conhecidos, regra, situação de decisão. |
| Ações | ID, campos de entrada/saída, evento/gatilho, pré-condições, validação, efeito, modalidade, mensagens, operação e cenários. |
| Eventos | ID, emissor/ação, momento, payload conhecido, efeito observável/consumidores quando pertinentes. Evento de interface não prova barramento implementado. |
| Estados/transições | IDs, cenário/acionamento de revisão, representação, ação/evento, estado de origem/destino, dados/foco preservados. |
| Regras/fórmulas | ID, fonte, entradas, fórmula/limites quando sustentados e cenários com resultado esperado. |
| Consultas/operações | ID, intenção, entrada/saída, conceitos/campos tocados, API existente/proposta/pendente, vínculo ao contrato, situação de verificação. |
| Dependências | Tela/componente/token/dado/operação necessário, proprietário e estado; destinos ausentes bloqueiam o fluxo afetado. |
| Aceite/evidências | Cenários, critérios, modalidade de teste, resultado e referência real; ausência de execução explícita. |
| Decisões | Conflitos, propostas, hipóteses e pendências com impacto e fonte; aprovações por versão. |

## Origem e decisão são dimensões diferentes

- `persistido`: campo do modelo/schema declarado como armazenado; a fixture representá-lo não prova banco real.
- `derivado`: valor calculado com regra e entradas rastreadas; não cria coluna automaticamente.
- `visual`: estado de apresentação sem dado de domínio persistido, por exemplo expansão de painel.
- `proposto`: novo elemento sem origem ainda estabelecida. Registre motivo e efeito; não o apresente como campo existente.

Use também `decisao: decidido|proposto|hipótese|pendente`: um cálculo pode ser derivado e sua fórmula ainda ser proposta. Não confunda `origem: persistido` com `modalidade: real existente`.

Para operações, separe `situacao: existente|proposta|pendente` de `verificacao: documental|executada|não executada`. API descrita mas não chamada é existente documentada, não teste executado; resposta de operação proposta é uma simulação. Não invente endpoint, verbo HTTP ou contrato de resposta para aparentar completude.

## IDs e vínculos

IDs devem ser únicos no pacote ou ter namespace explícito por tela. Toda referência a campo, ação, região, evento, regra, estado e cenário precisa resolver. Fonte semântica pode ser `Pedido.quantidade`; `tabela.coluna` exige schema conhecido. Vínculo físico desconhecido usa null/pendência, sem fabricar tabela.

Em HTML, `data-regiao`, `data-acao`, `data-campo` e `data-estado` podem referenciar esses IDs. Outro frontend pode usar IDs/seletores equivalentes documentados. Não exija atributos ou construções próprias de Claude Design em outros executores.

## Conferência significativa

Confronte no sentido inverso também: controle exposto deve aparecer no manifesto; ação obrigatória do contrato deve ter implementação/localização. Rejeite referência órfã, campo derivado sem regra, ação sem efeito/saída, transição sem cenário, destino pendente tratado como pronto e operação simulada descrita como backend real. A leitura desses vínculos é documental; confirmar que um botão funciona exige execução.

Não há schema JSON rígido universal: preserve a estrutura do projeto, com os vínculos acima verificáveis e um mapeamento de nomes se os campos forem diferentes.
