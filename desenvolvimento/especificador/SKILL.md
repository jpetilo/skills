---
name: especificador
description: "Gere PRD e SDD inicial rastreáveis a partir de uma síntese validada e materiais do produto, antes da modelagem física. Preserve decisões aprovadas, identifique hipóteses e lacunas e registre o refinamento posterior pelo modelo de dados e pelo protótipo. Não exige DDL pronta nem implementa o sistema."
---

# Especificador

Transforme o entendimento validado em **PRD e SDD inicial**, com conteúdo suficiente para orientar Modelador e Prototipador. Este é o contrato adaptado solicitado pelo usuário, anterior à modelagem; não execute a fase `dominio-problema` do Agentic Builder como se fosse esta entrada. A origem e a diferença estão em [ORIGEM.md](ORIGEM.md).

## Entrada e autoridade

- Receba a síntese aprovada, sua mensagem/versão de aprovação e os materiais pertinentes. Se a entrada ainda for rascunho, preserve esse status. Não repita a entrevista nem reabra decisões resolvidas sem contradição material.
- **Não exija banco, DDL, esquema físico, PROJECT.md ou pacote M1 fechado para produzir o PRD/SDD inicial.** Modelo existente é evidência adicional, não pré-requisito. Não execute scripts herdados da fase pós-DDL.
- Preserve a intenção e rastreie requisitos às decisões do usuário. Separe `decidido`, `proposto`, `hipótese` e `pendente`. Uma escolha de representação, arquitetura ou tecnologia não se torna aprovada por aparecer no SDD.
- Use o destino combinado. Sem destino autorizado, apresente o conteúdo na conversa e resolva onde gravar antes de criar arquivos; não grave documentos do produto no repositório de uma skill.

## Produza os documentos

Use o [conteúdo dos documentos](references/prd-sdd.md), proporcional ao produto.

1. **PRD:** problema, público, resultado esperado, recorte, capacidades e exclusões efetivamente decididas, jornadas relevantes e critérios observáveis de sucesso. Identifique requisitos funcionais, regras e necessidades de qualidade materiais às decisões; não invente metas de desempenho, segurança, acessibilidade ou disponibilidade para preencher seções.
2. **SDD inicial:** comportamento, regras, estados, fluxos e interfaces já sustentados; conceitos/relações conhecidos e a fronteira de simulação versus operação real. Registre decisões técnicas confirmadas e as pendentes com impacto e etapa de resolução. Não antecipe tabelas, colunas, endpoints ou arquitetura que dependam da modelagem ou de uma decisão ainda não tomada.
3. **Decisões e pendências:** registre a fonte, consequência, condição de fechamento e quem/qual etapa pode resolver cada lacuna relevante. Hipóteses permanecem hipóteses, mesmo aceitas para exploração.

Use IDs estáveis dentro da versão para requisitos, regras e critérios. Referencie as regras pelo ID em vez de manter cópias contraditórias. Não confunda identificação de requisitos derivada da síntese com aprovação humana de texto novo. Pergunte uma decisão bloqueante por vez, com opções concretas e recomendação quando pertinente; prossiga com pendências não bloqueantes explícitas.

## Prepare a modelagem e a prototipação

Entregue ao Modelador PRD/SDD inicial, conceitos conhecidos, regras, fontes, dúvidas de cardinalidade e decisões técnicas abertas. A ausência de DDL não bloqueia o modelo conceitual. O SDD inicial pode conter lacunas declaradas sem fingir arquitetura fechada.

Após a modelagem, incorpore somente a versão e decisões efetivamente validadas: atualize o SDD com entidades, relações e regras refinadas, mantendo deltas e origem. Decisões físicas dependem de pedido e motor confirmados; a criação de documentos não autoriza criar banco.

Entregue ao Prototipador as versões correntes dos dois documentos, o modelo disponível e a referência visual indicada. Identifique quais partes estão aprovadas ou ainda propostas. Descobertas do protótipo podem refinar comportamento e experiência; alterações materiais voltam à validação, sem substituir silenciosamente decisões.

## Confira e entregue

Use os [critérios de pronto](references/criterios-pronto.md). Entregue `PRD.md`, `SDD.md` e registro de decisões/pendências, ou seus equivalentes no formato combinado, com status e versão próprios. A síntese validada não aprova automaticamente os documentos derivados. Peça validação do conteúdo quando houver suficiência para a próxima etapa.

Não gere aplicação, modelo físico, DDL, migrations, roadmap executado ou testes de produto automaticamente. As referências históricas da antiga cópia pós-DDL continuam preservadas para consulta de origem; não são pré-condições desta adaptação, nem transformam `verificar-dominio.py` em validador de PRD/SDD.
