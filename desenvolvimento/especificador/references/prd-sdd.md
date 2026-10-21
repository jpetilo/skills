# Conteúdo proporcional de PRD e SDD inicial

## PRD

- Identidade, versão, status e fonte da intenção/aprovação de entrada.
- Problema, público, resultado pretendido e recorte escolhido.
- Capacidades e limites, diferenciando requisito aceito de sugestão; exclusões somente quando sustentadas.
- Jornadas/tarefas, requisitos funcionais e regras de negócio identificados por IDs.
- Critérios de aceite observáveis ligados a esses IDs; sinais de sucesso sem números inventados.
- Restrições e necessidades não funcionais materialmente relevantes, fontes e lacunas.
- Dependências e pendências que condicionam o produto ou a próxima etapa.

## SDD inicial, anterior ao modelo físico

- Versão/status, PRD de origem e recorte do desenho.
- Comportamentos, eventos, estados e fluxos sustentados pelas decisões; bordas relevantes ainda abertas.
- Conceitos e relações conhecidos, sem declarar cardinalidades ou campos físicos não confirmados.
- Interfaces/contratos de interação conhecidos e pontos de integração; nomes de endpoints, payloads, tipos físicos e arquitetura continuam pendentes quando não decididos.
- Simulação e dados de exemplo versus autoridade, persistência e operação reais esperadas.
- Decisões técnicas confirmadas e sua origem. Cada decisão técnica pendente informa impacto e momento de resolução; não adotar stack por hábito.
- Rastreabilidade requisito → regra → critério/cenário → conceito/tela quando já conhecido.
- Pontos para refinamento após Modelador e Prototipador, com atualização de versão e deltas.

Não preencher seção sem evidência. `Não aplicável`, `proposto` e `pendente` têm significados diferentes. Especificação inicial suficiente não significa contrato de implementação completo.
