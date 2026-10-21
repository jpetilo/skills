---
name: modelador
description: "Transforme uma síntese de domínio, escopo validado ou PRD inicial em modelo conceitual ou lógico e diagrama ER editável, renderizado e conferido. Explicite relações, cardinalidades, regras, fontes, hipóteses e pendências. Use para compreender e revisar modelos; não cria banco, migrations ou aplicação automaticamente."
---

# Modelador

Modele o domínio solicitado com fidelidade às fontes e mostre um diagrama que a pessoa consiga revisar. Trabalhe a partir do escopo existente; não refaça a descoberta nem amplie funcionalidades para completar um desenho. Esta skill é independente de plataforma, motor de banco, setor e outras skills.

## Entrada, destino e confiança

- Aceite síntese validada, PRD inicial ou descrição suficiente. PRD e SDD formais não são pré-requisitos. Preserve o estado real da entrada: uma proposta não vira requisito aprovado por entrar no modelo.
- Identifique a versão ou mensagem de origem e atribua referências locais estáveis às decisões e regras. Não invente falas, assinatura ou aprovação. Leia somente materiais pertinentes ao pedido.
- Confirme o destino somente quando não estiver indicado ou autorizado. Nunca use o repositório da própria skill ou de outra skill como pasta do produto. Sem destino para arquivos, ofereça a proposta na conversa enquanto resolve essa lacuna.
- Diferencie `decidido`, `proposto`, `hipótese` e `pendente` por item. Separe o conceito informado da escolha de representá-lo como entidade, atributo ou associação; uma representação nova continua proposta.

## Escolha o nível solicitado

**Conceitual, por padrão:** conceitos e significados, limites, associações, cardinalidades sustentadas, responsabilidades, regras e eventos relevantes. Não transforme cada substantivo em entidade. Não acrescente IDs, FKs, tipos SQL ou estruturas de autenticação sem necessidade e evidência.

**Lógico, quando solicitado:** atributos semanticamente necessários, identificadores, opcionalidade, unicidade, normalização pertinente, resolução de N:N e correspondência com o conceitual. Explique as decisões; não imponha tabelas de parâmetros ou histórico por rotina. Aplique as convenções herdadas de nomes, chaves e auditoria com compatibilidade explícita de escopo/motor. Mantenha independência do motor, salvo restrição explícita.

**Físico, somente por pedido explícito:** registre o motor e a versão confirmados e apresente escolhas físicas como outra camada. Gerar esse modelo não autoriza conectar a banco nem executar DDL, migrations, seeds ou alterações de dados. Encaminhe execução a uma tarefa separada e autorizada.

Uma tecnologia já escolhida pode ser registrada como restrição futura sem converter prematuramente o modelo conceitual em esquema físico.

## Convenções do autor

Antes de nomear entidades/atributos no lógico, leia [convenções herdadas](references/convencoes-modelagem.md). Aplique singular/snake_case, PK `entidade_id`, FKs pelo nome referenciado, prefixos seletivos, auditoria e mnemônicos. Mostre os mesmos campos na fonte editável, diagrama e dicionário; nomes genéricos `id` ou `*_ref` não atendem a esse padrão. Sem identidade de autoria/autenticação disponível, não imponha `criado_por`/`alterado_por` ou entidade de usuário: registre a exceção ao padrão da origem. Datas de criação/alteração são independentes. Separe tipos semânticos de materialização por motor. A camada conceitual mantém a correspondência dos termos com os nomes canônicos.

## Derive e confira o modelo

1. Extraia conceitos e regras das fontes. Preserve termos do usuário e explique sinônimos relevantes. Mapeie cada conceito, relação e regra à origem; assinale decisões de representação propostas.
2. Para cada relação relevante, descreva os dois sentidos, mínimo/máximo e a regra que os sustenta. Não infira obrigatoriedade, exclusividade, propriedade, identificação ou cascata só pela aparência do desenho. Use `?` na descrição de uma cardinalidade desconhecida e registre a lacuna; nunca codifique esse símbolo como cardinalidade Mermaid ER válida.
3. Distinga associação estrutural, responsabilidade, alinhamento e dependência de cálculo. Uma ligação de alinhamento não implica agregação, compartilhamento ou atualização automática.
4. Relacione as regras de comportamento aos conceitos: condições, eventos, estados, cálculos e efeitos observáveis. Um ER não substitui essas regras. Quando necessário ao pedido, complemente com fluxo ou estados sem iniciar projeto de interface ou arquitetura.
5. Confira contradições, vínculos órfãos, ciclos indevidos, dupla contagem, cardinalidade versus regra e perda de significado entre níveis. Atributos derivados precisam ser identificados como derivados; sua forma de armazenamento não é decidida pelo modelo conceitual.
6. Pergunte uma decisão bloqueante por vez, com opções concretas, exemplos e recomendação quando úteis. Registre a resposta e avance no mesmo turno. Se a lacuna não bloquear a visualização, entregue rascunho com proposta ou pendência explícita; não finja que a entrevista ocorreu.

Pare quando houver suficiência para a próxima etapa pedida. Não busque completude universal, nem transfira para o usuário decisões que as fontes já resolvem. Modelos de legado descrevem o observado como evidência, separadamente do desejado.

## Gere, renderize e inspecione

Consulte [notação e ferramentas](references/diagramas.md) antes de gerar Mermaid ou usar o renderizador local. A documentação oficial do Mermaid prevalece sobre exemplos de terceiros.

- Preserve fonte editável e documento de interpretação. Mermaid `erDiagram` é preferido quando a notação consegue expressar o que está sustentado. Quando identificação ou cardinalidades estiverem abertas, não escolha valores silenciosamente para satisfazer o parser: use uma visão conceitual com rótulos explícitos e liste as lacunas. O renderizador próprio usa cardinalidades textuais e não se apresenta como parser Mermaid.
- Use Mermaid CLI oficial local somente se já disponível. Não instale dependências nem envie conteúdo a renderizadores online sem autorização específica. A alternativa incluída usa Python padrão para SVG e Mermaid textual; no Windows, PNG pode ser gerado com PowerShell e System.Drawing já disponíveis.
- Execute o renderizador sobre a fonte real. Abra a imagem gerada com uma ferramenta de imagem ou navegador e confira legibilidade, nomes, relações, cardinalidades, legenda e ausência de cortes ou sobreposições. Corrija até três vezes; se ainda falhar, entregue fonte e relate o bloqueio, sem chamar de visualmente conferido.
- Separe evidência semântica, validação estrutural/sintática e inspeção visual. Uma imagem bonita não valida as decisões, e um SVG gerado não prova que foi inspecionado. Registre a tecnologia usada e limitações da renderização.

## Entrega e transição

Entregue, conforme o pedido, o modelo em texto com fontes e regras, a fonte editável (`.mmd` e/ou `.json`), SVG e uma imagem de visualização quando suportada. Explique as pendências que impedem usar o modelo como contrato e as representações ainda propostas. Exiba o diagrama na conversa ou forneça o arquivo efetivamente renderizado; não entregue apenas um link para um renderizador externo.

Mantenha o novo modelo como `rascunho` até aprovação explícita da versão apresentada. Entrada validada não significa modelo derivado validado. Peça uma única aprovação do conteúdo quando houver suficiência, preservando hipóteses aceitas como hipóteses. Não crie PRD, SDD, protótipo, banco ou aplicação automaticamente. A saída serve de entrada rastreável para essas etapas, não de autorização para executá-las.

As [origens](references/origens.md) explicam os materiais consultados e o que foi deliberadamente excluído. Não é necessário instalar ou invocar as skills de origem para usar este pacote.
