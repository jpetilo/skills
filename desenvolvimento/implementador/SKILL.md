---
name: implementador
description: "Entrada fina para implementar uma fatia funcional contratada usando o orquestrar-roadmap do Agentic Builder instalado, preservando preflight, roadmap, integração, revisões e E2E. Explicita incompatibilidades de perfil e não inventa um modo nativo de onda única, backend, autenticação ou deploy."
---

# Implementador

Use o motor real orquestrar-roadmap (dependência local; consultar `DEPENDENCIAS.md` na raiz), lendo-o integralmente ao iniciar. Esta entrada não copia nem substitui o controlador do plugin. As [dependências e limites](references/dependencias.md) fazem parte do contrato.

## Antes da execução

Receba PRD/SDD correntes, modelo de dados e protótipo/handoff aprovados, escopo da fatia, raiz autorizada do projeto e restrições técnicas confirmadas. Confira a correspondência entre o que foi aprovado e os artefatos nativos exigidos pelo plugin; não considere textos resumidos um substituto automático de um pacote M1 fechado.

O gerar-roadmap (dependência local; consultar `DEPENDENCIAS.md` na raiz) exige `docs/07-handoff/phase-1-exit.yaml` completo, casos de uso/núcleos e dependências, perfil existente/válido e `prototype-screen-contracts.yaml` sem gaps, com continuidade por tela. O controlador ainda exige roadmap com itens e `.agentic/m2/harness/test-contract.yaml` pronto para iniciar. Sem isso, relate a lista completa de faltas; não fabrique aprovações ou marque gates como concluídos.

Confira se o perfil atende ao motor, autenticação e runtime escolhidos. Não selecione um perfil Supabase por aproximação para um projeto SQLite, nem adicione login/tenant para satisfazer o perfil. Se não houver perfil compatível, pare antes de executar e apresente a incompatibilidade e a adaptação mínima necessária para decisão; não modifique o plugin inteiro ou crie um novo motor nesta entrada.

## Fatia compacta, sem enfraquecer o processo

O pedido por uma única onda é uma intenção de recorte. O controlador não tem flag de “onda única total”: ele executa as ondas definidas no roadmap. Uma fatia pode caber em uma onda funcional somente se as dependências e os contratos reais permitirem. Não renumere ou compacte ondas à força, nem elimine prelúdios necessários, revisões, integração ou testes para prometer prazo.

Use o preflight e compilador reais quando a tarefa autorizar executá-los. Confira o plano resultante antes de afirmar a quantidade de ondas. Mudança material do recorte ou do perfil é decisão explícita, não ajuste escondido.

## Execução pelo motor instalado

Depois do preflight e somente com autorização de implementação, use o controlador nativo (dependência local; consultar `DEPENDENCIAS.md` na raiz), com os argumentos reais `iniciar`, `estado`, `abrir`, `fechar` e `onda ... checkpoint` conforme a skill original. Comandos de testes vêm exclusivamente do test-contract do projeto; não os duplique com defaults nesta entrada.

Mantenha um responsável pela onda. Implemente a fatia vertical completa por meio dos contratos de implementar-funcionalidade (dependência local; consultar `DEPENDENCIAS.md` na raiz) e integrar-funcionalidades (dependência local; consultar `DEPENDENCIAS.md` na raiz): interface, dados/persistência contratados, regras, estados, visual, revisões e evidências. Não replique o protótipo em outra árvore nem transforme simulação em persistência real por descrição.

E2E ausente, incompleto ou falho mantém o trabalho aberto. Mesmo se o checkpoint nativo não tratar um SKIP como falha, não declare a fatia funcional demonstrada sem comprovar a execução dos seus cenários esperados. Não escreva completion/quality-final/marco-exit como PASS por inferência.

Quando o controlador devolver a obrigação de qualidade global, use o Testador como entrada dessa mesma etapa. Não duplique a avaliação global porque há dois nomes de skill. A aplicação pode estar pronta para avaliação final sem que a orquestração nativa já esteja `concluido`; somente o fechamento real de seus gates permite esse status.

Entregue ao Testador versão/arquivos, ambiente, casos esperados, comandos canônicos, fixtures e evidências da integração/E2E, junto de qualquer falha reproduzível. Correções recebidas voltam à fatia afetada e são revalidadas. Deploy, produção e gastos externos continuam fora desta entrada.
