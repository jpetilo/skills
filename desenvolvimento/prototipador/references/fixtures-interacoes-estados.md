# Fixtures, interações e estados reproduzíveis

Use na preparação dos dados e do comportamento. Não há domínio ou quantidade de estados padrão.

## Derivação das fixtures

1. Liste fontes e decisões válidas: síntese do Investigador, PRD/SDD, modelo/dicionário, schema e API disponíveis. Separe divergência material de lacuna; registre cada uma e resolva a que muda regra, cálculo, relação ou tarefa antes de codificá-la. Não escolha silenciosamente a fonte mais conveniente.
2. Reutilize IDs canônicos de entidades/campos/regras. Dê IDs estáveis aos registros fictícios e reutilize-os entre telas; rótulo da interface não renomeia coluna física. Referências apontam para registros presentes no mesmo conjunto ou dependência explícita.
3. Preserve cardinalidades e limites sustentados. Cardinalidade não conhecida permanece pendência, não vira requisito para acomodar a fixture. Não gere dado pessoal real nem apresente nomes, eventos ou histórico fictícios como observação de produção.
4. Faça uma amostra pequena suficiente para as tarefas e estados aplicáveis: principal, coleção vazia, pesquisa sem resultado, limite válido, entrada inválida e falha simulada. Fixture inválida usada para testar rejeição fica isolada, identificada como negativa; não corrompa o conjunto principal.
5. Registre para cada cenário: IDs de entrada, ação, regra/fórmula, resultado esperado, tolerância/arredondamento/unidade/data de referência quando relevantes, e estado esperado. Sem regra suficiente, declare pendência; não invente fórmula.
6. Declare armazenamento, versão do conjunto e reset reproduzível. Memória ou localStorage são escolhas de simulação: comportamento ao recarregar/reiniciar precisa estar no contrato. Não sobrescreva dados existentes de demonstração sem pedido; reset afeta só o conjunto/namespacing autorizado.

## Contrato de interação por ação aplicável

| Momento | O que explicitar |
| --- | --- |
| Abrir | Contexto/registro selecionado, estado inicial, carregamento e foco inicial pertinente. |
| Editar | Campos editáveis e somente leitura, rascunho versus valor confirmado, alteração relevante em outras regiões. |
| Validar | Regra sustentada, momento da validação, campo, mensagem curta, como corrigir e o que preserva. |
| Salvar/confirmar | Pré-condições, efeito simulado/real/pendente, indicação de processamento, prevenção de duplo envio quando pertinente e resultado. |
| Cancelar/voltar | Destino, descarte ou preservação de rascunho conforme contrato, último estado válido e retorno de foco. |
| Falhar/repetir | Mensagem essencial, entrada preservada, ausência de confirmação falsa, recuperação e efeito de repetir. |
| Navegar | Dados/contexto preservados e próxima tela/estado; não simular destino inexistente como ação concluída. |

Não transforme uma ação simples em um formulário ou modal por obrigação deste quadro. Se não há edição ou cancelamento aplicável, registre N/A e motivo no contrato. Medição e edição estrutural são operações diferentes apenas quando a fonte do domínio as distinguir.

## Matriz de estados por tela

Para cada estado pertinente, registre ID, regra/origem, cenário/fixture, acionamento, elemento/mensagem visível, ações permitidas, transição de saída, dados preservados e evidência. Diferencie vazio inicial de pesquisa sem resultado quando isso mudar a orientação ou ação possível. Carregando, inválido, erro, sucesso e indisponibilidade dependem dos fluxos reais; login, permissão e exclusão não são estados obrigatórios universais.

Cada acionamento de revisão deve ser reproduzível: modo/rota de revisão, fixture e sequência, parâmetro de cenário ou mecanismo equivalente documentado. Esse mecanismo fica fora da operação normal, não chama mutações reais para produzir erro nem altera silenciosamente o conjunto válido. Sair da revisão devolve o estado definido no contrato; simulação não persiste erro ou dado inválido como último estado válido.

Use IDs iguais na interface/anotações, manifesto, matriz e cenários. Quando uma transição depender de backend futuro, simule apenas o resultado declarado e marque essa fronteira. Estados previstos mas não construídos são pendentes; não conte como cobertura executada.
