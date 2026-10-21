# Skills de desenvolvimento

Seis skills do autor, publicadas em [desenvolvimento](desenvolvimento), cada uma em sua pasta. Os originais instalados no computador do autor foram preservados. Este repositório não contém o plugin Agentic Builder completo nem instruções internas de plataforma.

| Skill | Papel |
|---|---|
| [Investigador](desenvolvimento/investigador/SKILL.md) | Compreender domínio, relações, regras e decisões até suficiência |
| [Especificador](desenvolvimento/especificador/SKILL.md) | Derivar PRD e SDD inicial de síntese validada |
| [Modelador](desenvolvimento/modelador/SKILL.md) | Modelos, dicionário e diagrama verificável |
| [Prototipador](desenvolvimento/prototipador/SKILL.md) | Protótipo rico e contrato rastreável por tela |
| [Implementador](desenvolvimento/implementador/SKILL.md) | Entrada para execução funcional e integração contratadas |
| [Testador](desenvolvimento/testador/SKILL.md) | Evidência reproduzível, falhas, correção e regressão |

## Baixar e usar

[Baixar ZIP](https://github.com/jpetilo/skills/archive/refs/heads/main.zip), extrair e renomear a pasta externa `skills-main` para `skills`, ou clonar:

```powershell
git clone https://github.com/jpetilo/skills.git skills
```

Não sobrescrever uma pasta existente. Para seguir a palestra, deixe `skills` e `Uninassau-2026` como pastas irmãs. Abra Uninassau-2026 no agente e peça explicitamente:

```text
Leia ../skills/desenvolvimento/investigador/SKILL.md e suas referências.
Siga esse método para a etapa solicitada; não execute outras etapas automaticamente.
```

Isso utiliza os arquivos locais, sem exigir registro global. O agente precisa ter acesso de leitura ao clone irmão. Se preferir instalação automática no catálogo de um produto, siga o formato aceito por ele; a cópia não instala plugins ou suas dependências.

## Instalação opcional por projeto no Codex

A documentação oficial descreve skills de projeto em `.agents/skills` e pessoais em `$HOME/.agents/skills`: [fonte](https://developers.openai.com/codex/learn/best-practices). Exemplo abaixo, a executar pelo aluno **na raiz do projeto que receberá as skills**, com o clone `../skills` já disponível:

```powershell
$names = @('investigador','especificador','modelador','prototipador','implementador','testador')
foreach ($name in $names) {
  $source = Join-Path '../skills/desenvolvimento' $name
  $target = Join-Path '.agents/skills' $name
  if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) { throw "Fonte ausente: $name" }
  if (Test-Path -LiteralPath $target) { throw "Destino existente: $target; comparar antes de copiar." }
}
New-Item -ItemType Directory -Path '.agents/skills' -Force | Out-Null
foreach ($name in $names) {
  Copy-Item -LiteralPath (Join-Path '../skills/desenvolvimento' $name) -Destination (Join-Path '.agents/skills' $name) -Recurse
}
```

Abra uma nova sessão do agente e confira se as seis entradas foram reconhecidas. Se o catálogo não as mostrar, use leitura explícita do SKILL.md e confira a configuração do produto; não presuma ativação. Em outros agentes, siga sua documentação de instalação ou use leitura explícita. Nenhuma instalação global foi realizada por esta publicação.

## Limites e exemplo

[Dependências e origens](DEPENDENCIAS.md) são parte da distribuição. Implementador e Testador são entradas finas de um processo maior; copiar só esses textos não instala seu motor. A demonstração [Uninassau 2026](https://github.com/jpetilo/Uninassau-2026) registra uma exceção local de Python/SQLite, não uma aprovação fictícia dos gates nativos.

Publicação pública solicitada pelo autor. Nenhuma licença geral open source foi escolhida automaticamente; os avisos e atribuições específicos permanecem nos arquivos. A publicação não declara validação profissional autônoma ponta a ponta das seis skills.
