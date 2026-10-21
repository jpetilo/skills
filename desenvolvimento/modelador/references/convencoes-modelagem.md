# Convenções herdadas da modelagem-dados

Aplicar no modelo lógico e nos nomes técnicos mostrados em diagramas. A visão conceitual preserva o vocabulário de domínio e explicita sua correspondência com os nomes canônicos; não é justificativa para omitir o padrão solicitado.

Fonte normativa local: Agentic Builder 0.9.3, `skills/modelagem-dados` 2.2.1, `references/convencoes-nomenclatura.md`, conferida com `SKILL.md`, `matriz-decisao.md`, packs de motor e `persona.md`. Originais preservados. O registro de origens deste pacote informa o caminho exato. Não importar automaticamente o pipeline de DDL ou um motor diferente do escolhido.

## Nomes e chaves — aplicar desde o lógico

- Entidade: substantivo singular, `snake_case` minúsculo (fonte, linha 7).
- PK lógica: `entidade_id`; nunca `id` isolado ou camelCase (linha 8). Tipo/geração da chave é outra decisão, não determinada pelo nome.
- Campo genérico ambíguo: `entidade_campo`, como `empresa_nome` e `resultado_chave_descricao` (linha 9). Campo semanticamente específico permanece sem prefixo artificial (linha 10); justificar classificações que afetem o dicionário.
- FK: `entidade_referenciada_id`; autorreferência acrescenta o papel da relação, como `objetivo_alinhado_id` (linha 11). Conferir o destino PK/UK; não usar `*_ref` como substituto do padrão.
- Associativa N:N, se realmente necessária: `entidade1_entidade2` e PK `entidade1_entidade2_id` (linha 12). Não inventar N:N para preencher a convenção.
- Gênero de flags acompanha a entidade (linha 13). Não acrescentar `ativo`, exclusão lógica ou histórico por rotina.

## Auditoria — representar e verificar compatibilidade

A origem exige em entidade não seed/parâmetro `criado_em`, `criado_por` (FK usuario), `alterado_em` e `alterado_por`, sem prefixo (linhas 15 e 26). Esta adaptação aplica a seguinte **exceção condicional explícita**, solicitada pelo usuário:

- Quando não houver identidade de autoria/autenticação disponível, **não incluir `criado_por` nem `alterado_por`**. Registrar a omissão justificada no modelo/dicionário; não deixar esses campos como pendência obrigatória e não criar usuário/login para satisfazê-los.
- `criado_em` e `alterado_em` são metadados temporais independentes. Não removê-los automaticamente junto com autoria; sua geração/atualização depende do desenho físico.
- Quando houver identidade real disponível, aplicar o contrato de autoria pertinente ao projeto. A ausência de uma tela de login isoladamente não prova ausência de identidade; usar o contexto confirmado.

Não transformar FK de autoria em texto silenciosamente nem usar responsável de negócio como autor da alteração. Essa exceção é à exigência da origem, não uma afirmação de que timestamps registram quem alterou o dado.

## Mnemônicos e objetos

Mnemônico único de quatro letras por entidade; conferir primeiro `docs/03-banco/mnemonics.md` se existir (linhas 19–20). Se o produto utiliza outro destino autorizado, manter ali um dicionário explícito e apontar a ausência do caminho nativo, sem criar uma árvore de processo não solicitada. Objetos seguem `tipo_mnem_nn` minúsculo, sequência por tipo/entidade (linhas 21–22). Exemplos de origem: `pkc_objt_01`, `fkc_objt_01`, `idx_objt_01`. Registrar mnemônicos no lógico; constraints/índices físicos não são executados nesta etapa.

## Tipos, derivações e física

- No dicionário lógico, distinguir identificador, texto, data, momento, número decimal e referências. Registrar tamanho/precisão pendentes, sem inventar limites (linha 41).
- A matriz D-01 decide geração/tipo de PK conforme exposição, escala e motor. Não aplicar UUID/identity/auto_increment de outro motor por analogia. Sem pack para o motor escolhido, apontar a lacuna.
- A origem determina calculados em views, nunca colunas (`SKILL.md`, Passo 2). Identificar os derivados no lógico e prever views na materialização; não representá-los como colunas armazenadas. Não criar views sem autorização de DDL.
- Política explícita `ON DELETE`, índices, triggers/`ON UPDATE`, comments, defaults e enforcement são decisões da materialização física. Registrar que faltam; não fingir validação em motor por existir um ER.
- `BIT(1)` versus boolean, `DATE`, `NUMERIC(p,s)`, `timestamptz`/`DATETIME` e UUID/identity têm aplicabilidade por motor. `criado_em`/`alterado_em` são momentos, não as datas do ciclo. Não transplantar os packs Postgres/MySQL para SQLite.

Antes de entregar: conferir nomes de entidade, PK/FK, campos genéricos/específicos, auditoria e mnemônicos no dicionário **e no diagrama editável**. Diferenciar convenção aplicada de regra de negócio proposta. Enumerar qualquer desvio ou conflito pendente; não declarar conformidade completa se houver lacuna material.
