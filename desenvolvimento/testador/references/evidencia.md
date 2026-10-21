# Dependências e interpretação dos resultados

Dependência instalada: `DEPENDENCIA_LOCAL`. Esta entrada não copia o avaliador funcional nem substitui seu orquestrador. Autor do plugin identificado como Jefferson; licença não identificada nos arquivos inspecionados. Os originais permanecem intactos.

- Quality Orchestrator (dependência local; consultar `DEPENDENCIAS.md` na raiz): avaliação especializada única após estabilização das ondas; achados obrigatórios retornam à implementação.
- functional-e2e-agent (dependência local; consultar `DEPENDENCIAS.md` na raiz): todas as ações esperadas, base explícita, hard gate, contexto limpo e porta dinâmica; não corrige código e não é avulso.
- checkpoint-onda.py (dependência local; consultar `DEPENDENCIAS.md` na raiz): deriva escopo do roadmap e comandos do test-contract. A versão inspecionada pode marcar `SKIP` quando o filtro não encontra testes e não contar isso como falha nativa. O wrapper não altera esse motor, mas exige cobertura dos cenários esperados para seu próprio veredito.
- gerar-test-contract.py (dependência local; consultar `DEPENDENCIAS.md` na raiz): comandos canônicos e perfil do projeto. Não executar sem a tarefa de preparação/implementação autorizar.
- next16-supabase.yaml (dependência local; consultar `DEPENDENCIAS.md` na raiz): exemplo existente usa Playwright Chromium, um worker e `case_regex`; inclui dependências específicas de Supabase. Não é perfil SQLite nem configuração universal de testes visíveis.

## Evidência mínima por cenário

ID/fonte, revisão do produto, ambiente, fixture/pré-condição, comando/seleção, passos, esperado, observado, resultado, saída e referência existente de captura/trace/relatório quando aplicável. Conte o que rodou; não infira execução da existência de um cenário escrito.

O relatório deve manter a diferença entre falhou, bloqueado, ignorado e não executado. PASS com zero cenários esperados sem justificar escopo é inconclusivo. Um cenário obrigatório ignorado/não encontrado mantém a cobertura incompleta. Um N/A fundamentado não vira cenário executado.

A nova cadeia documental não satisfaz automaticamente o preflight M1/M2 do plugin. Perfil compatível, artefatos nativos e capacidades do executor continuam condições de execução; não foram construídos ou exercitados nesta preparação.
