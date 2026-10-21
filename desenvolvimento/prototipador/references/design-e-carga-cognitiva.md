# Design system, tokens e carga cognitiva

Leia ao iniciar a direção visual e ao revisar uma tela. Reutilize a fonte informada e respostas existentes; não inicie outro levantamento de marca quando já houver material suficiente.

## Entrada e decisão

Aceite link acessível, arquivo de tokens, biblioteca existente ou referência visual. Inspecione o material pertinente antes de descrevê-lo. Não instale biblioteca, fonte ou pacote nem transfira materiais a serviço externo sem autorização necessária ao caso.

Se faltar a fonte, faça a pergunta curta prevista no SKILL.md. Se houver apenas referência visual, extraia observações e proponha um conjunto mínimo; obtenha validação antes de tratá-lo como direção aprovada. Fonte inacessível ou família tipográfica não identificável permanece pendência. Continue preparação não visual sem fabricar identidade.

## Registro único de tokens

Use o formato que o projeto já adota, com os campos abaixo ou equivalentes. Cada tela referencia a versão do registro, sem recopiá-lo.

| Campo | Conteúdo |
| --- | --- |
| ID semântico | Nome estável por função; mapeie ao nome oficial se já existir. |
| Papel | Onde e para quê se usa, inclusive restrições semânticas. |
| Valor e unidade | Valor literal/alias real; ausente = pendente. Tipografia inclui família/fallback, tamanho, peso e entrelinha disponíveis. |
| Categoria | Cor; tipografia; espaçamento; raio; foco; elevação; movimento. |
| Procedência | Arquivo/link inspecionado e versão/trecho, ou decisão que originou a proposta. |
| Natureza | `oficial` (declarado na fonte), `derivado` (transformação explícita) ou `proposto` (escolha nova/inferida). |
| Derivação/decisão | Regra de transformação ou motivo; inferência de imagem é proposta, não token oficial. |
| Aprovação e uso | Estado, evidência de aprovação quando houver, componentes/telas afetados. |

Cores distinguem papéis pertinentes, por exemplo superfície, texto, ação, borda, foco e estados. Não imponha paleta, número de tons ou marca. Registre tokens de movimento com finalidade, duração e curva quando disponíveis; suporte à preferência de movimento reduzido. Registre foco visível, elevação e dimensões conforme fonte ou proposta identificada. Se a biblioteca não cobrir uma categoria relevante, liste a lacuna ou proponha valor; não afirme extração inexistente.

Reutilize componentes existentes. Uma extensão necessária precisa ter motivo, estados e aprovação afetada explícitos; não recrie um design system inteiro por ausência de um token.

## Revisão obrigatória da carga cognitiva

Avalie a tela na tarefa corrente, com dados de exemplo, não por limite de palavras arbitrário:

- Há uma ação principal compreensível e informação suficiente para executá-la?
- Cada instrução resolve uma dúvida real desse momento? Remova repetição e orientação concorrente.
- Cartões e resumos têm funções diferentes? Agrupe o que compete pela mesma atenção.
- Termos técnicos, origem dos dados e detalhes de implementação podem ir ao handoff ou ajuda contextual?
- Erro explica o que corrigir, junto ao campo/ação, com caminho de recuperação? Preserve o último estado válido.
- Campos obrigatórios, consequência relevante e rótulos acessíveis continuam perceptíveis? Não substitua rótulo essencial por tooltip, placeholder ou ícone isolado.
- Mensagens de status são perceptíveis por tecnologia assistiva quando aplicável; não dependa só de cor.
- Modo de revisão está separado da operação? Sua barra de simulação não disputa atenção com salvar/cancelar.
- O usuário pode descobrir detalhes progressivamente sem perder contexto, entrada ou foco?

Registre achado, decisão e evidência da revisão. Inspeção documental pode avaliar intenção e textos; só resultado renderizado permite avaliar composição, contraste, reflow e densidade visual. Nenhum score textual substitui essa inspeção.
