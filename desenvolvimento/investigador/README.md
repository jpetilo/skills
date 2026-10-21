# investigador
Skill de IA que transforma ideias em escopos claros por meio de uma conversa objetiva, com uma pergunta por vez, análise crítica de premissas e pesquisa quando necessário. Compatível com interação por texto e voz.

## Uso

O ponto de entrada é [SKILL.md](SKILL.md). Peça ao assistente que leia esse arquivo e use o Investigador para explorar uma ideia, delimitar um escopo ou retomar uma descoberta. Em um ambiente que já tenha cadastrado esta pasta como skill, use `$investigador`.

Exemplo de pedido: “Use o Investigador para delimitar esta ideia. Aproveite as decisões que já expliquei e faça uma pergunta por vez.”

A conversa aproveita o contexto, pesquisa fatos relevantes com as ferramentas disponíveis e apresenta recomendações sem tratá-las como decisões aceitas. A entrega é uma síntese proporcional ao pedido, com capacidades dentro e fora, critérios observáveis e hipóteses ou pendências visíveis. A intenção original fica separada da síntese.

O escopo permanece em rascunho até a aprovação explícita do conteúdo. Depois, fica validado; a skill não inventa assinaturas nem inicia implementação. Em voz, faz perguntas curtas e depende dos recursos de áudio ou transcrição da interface utilizada.

## Arquivos e disponibilidade

- [SKILL.md](SKILL.md): instruções autônomas em português.
- [references/sintese-escopo.md](references/sintese-escopo.md): guia opcional de entrega, conforme a complexidade.

Este repositório contém a elaboração local da skill. Clonar ou ler estes arquivos não instala, cadastra ou publica a skill automaticamente. Não há dependência obrigatória de scripts, de outro plugin ou de uma estrutura de projeto específica.

## Inspirações

As instruções foram redigidas para este projeto a partir da descoberta assistida de `delimitacao-escopo`, do Agentic Builder, e de ideias de [Architect](https://github.com/CodeWithClinton/architect_skill) e [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): aproveitar o contexto, investigar fatos e respeitar dependências entre decisões. O Investigador usa uma pergunta por vez por padrão e encerra quando o escopo estiver suficientemente claro; não exige a instalação dessas skills.
