# payment-support-ai-lab

Laboratório em Python para construir um copiloto de suporte a pagamentos e se preparar para a entrevista de Engenharia de IA em **09/12/2026**.

O cenário da demo é um pedido que continua pendente. O copiloto consulta runbooks fictícios, explica o que fazer com referências e, quando necessário, consulta o estado do pagamento em uma API simulada.

## Comece aqui

Abra o PowerShell na raiz deste repositório e rode:

```powershell
python --version
```

### Aula 1 · Percorrer eventos de pagamento

Crie `pagamentos.py` com estes dados:

```python
eventos = [
    {"pedido_id": 101, "status": "paid"},
    {"pedido_id": 102, "status": "failed"},
    {"pedido_id": 103},
]
```

1. Use `for evento in eventos:` para percorrer a lista. Cada evento é um dicionário.
2. Leia o ID com `evento["pedido_id"]` e o status com `evento.get("status")`. Quando a chave está ausente, `.get()` devolve `None`.
3. Use `if`, `elif` e `else` para decidir a ação. Imprima o ID e a ação com uma f-string, como `f"{pedido_id}: {acao}"`.
4. Rode `python pagamentos.py` e confira a saída:

```text
101: confirmar_pedido
102: registrar_falha
103: ignorar
```

**Desafio:** adicione um quarto evento com status `refunded` e retorne a ação `registrar_estorno`. Em seguida, extraia a decisão para a função `decidir_acao(evento)`. Ela recebe um dicionário e retorna a ação como texto. Mantenha a impressão no loop para que a função possa ser testada separadamente.

### Aula 2 · Preparar o ambiente de testes

Use estes comandos quando a função da primeira aula estiver pronta. Chamar o Python do ambiente virtual diretamente funciona no PowerShell sem depender da ativação do ambiente.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -q
```

Crie `test_pagamentos.py`, importe a função e use `assert` para verificar seu retorno. Cubra os casos `paid`, `failed`, `refunded`, status ausente e status desconhecido. Comece com um teste simples e depois use `pytest.mark.parametrize` para reaproveitar o mesmo teste com entradas diferentes.

### Aula 3 · Classes e objetos com eventos de pagamento

Depois de testar a função, crie uma classe `EventoPagamento` para praticar programação orientada a objetos (POO).

1. Use `class` para definir a classe e `__init__(self, pedido_id, status=None)` para guardar o ID e o status nos atributos `self.pedido_id` e `self.status`. Dentro de um método, `self` é o objeto que recebeu a chamada.
2. Crie dois objetos, um com `EventoPagamento(101, "paid")` e outro com `EventoPagamento(103)`. Leia seus atributos e confira que cada objeto tem seus próprios valores.
3. Escreva um método `descricao(self)` que devolva uma f-string com o ID e o status. Chame o método nos dois objetos e teste o resultado com `assert`.

Mantenha `decidir_acao(evento)` e seus testes. Na etapa de FastAPI, pratique herança ao declarar os modelos de entrada e saída com `BaseModel`. Na integração com Ollama, use uma classe `OllamaClient` para guardar a URL e o nome do modelo e reunir as chamadas em métodos.

### Sintaxe para praticar no laboratório

- **Eventos e testes.** Variáveis, números, strings, booleanos, `None`, listas, dicionários, condições, loops, funções, parâmetros com valor padrão, `return`, imports e `assert`.
- **Leitura de JSON.** Use `with` para abrir o arquivo e `try/except` para tratar arquivo ausente e JSON inválido.
- **Classes e API.** Pratique instâncias, atributos e métodos na Aula 3. Use anotações de tipo, herança e decoradores nas rotas e nos modelos de entrada e saída.
- **RAG.** Pratique compreensão de listas ao filtrar trechos e `sorted(..., key=...)` ao ordenar os resultados pela pontuação.

## Roadmap até a entrevista

| Período | Etapa | Critério de conclusão |
| --- | --- | --- |
| 26–29/11 | **Python, pytest e POO básica** · Praticar a regra de pagamentos, escrever testes, ler JSON e criar a classe da Aula 3. | Ler eventos de um arquivo JSON, tratar um arquivo inválido e passar os testes. Criar duas instâncias e verificar o retorno do método. Usar uma fixture quando houver dados compartilhados entre testes. |
| 30/11–01/12 | **FastAPI** · Reaproveitar a regra em `POST /payments/events` com modelos Pydantic de entrada e saída, anotações de tipo e um decorador de rota. | Demonstrar um evento válido e uma requisição fora do contrato em testes HTTP. |
| 02/12 | **Ollama pela VPN e saída estruturada** · Criar `POST /incidents/classify` e configurar o cliente Ollama com endereço e modelo pelo ambiente. Gerar o JSON Schema com Pydantic, enviar no campo `format` do Ollama e validar a resposta com a mesma classe Pydantic. | Rodar uma chamada real com um relato fictício e devolver `categoria`, `resumo` e `proxima_acao`. Testar resposta simulada válida, timeout e saída fora do contrato. |
| 03/12 | **Extração de documentos** · Ler um PDF com texto selecionável e extrair dados de um runbook. | Produzir JSON com código de erro, causa, procedimento e página de origem. Conferir os campos com o PDF. |
| 04–05/12 | **RAG e embeddings** · Dividir três runbooks fictícios em trechos, guardar metadados de origem e buscar por similaridade. | Confirmar um modelo de embeddings no Ollama da VPN, recuperar trechos relevantes e responder citando documento e seção ou página. Se faltar evidência, devolver uma resposta explícita de insuficiência. Começar com busca local e usar PostgreSQL com pgvector se houver tempo. |
| 06/12 | **Evals e logs** · Preparar os cinco casos abaixo e rodar os três de RAG. Registrar os trechos recuperados, a chamada da ferramenta quando houver, a validação do JSON e o tempo por etapa. | Comparar busca textual e vetorial com o mesmo modelo e prompt. Medir se o trecho esperado ficou entre os três primeiros, se a resposta é fiel à fonte, se o JSON é válido e quanto tempo o fluxo levou. Usar os logs para investigar uma falha. |
| 07/12 | **Roteamento e tool calling** · Começar com uma função Python de consulta de status somente leitura. Expor a função via MCP se houver tempo e usar LangGraph se o fluxo principal estiver pronto. | Rodar os dois casos de consulta de status abaixo e confirmar quando a função deve ser chamada. Tratar pedido inexistente e indisponibilidade da ferramenta. |
| 08/12 | **Simulação da entrevista** · Ensaiar a demo e revisar decisões técnicas. | Em cinco minutos, mostrar uma resposta com fonte, uma falha e o teste ou a avaliação que ajuda a explicá-la. |

Se o prazo apertar, priorize **Python, testes, FastAPI, saída estruturada com uma chamada real ao Ollama, RAG pequeno e cinco casos de avaliação**. MCP e o agente podem ficar como extensões da demo.

### Casos de avaliação da demo

Ao criar os runbooks, anote o documento e a seção esperados nos dois casos com fonte. Use essas referências para conferir se o trecho certo apareceu entre os três primeiros.

| Pergunta | Comportamento esperado |
| --- | --- |
| O que significa o erro `PAY-042`? | Recuperar o trecho do código no runbook fictício e citar a fonte. |
| O cliente pagou, mas o pedido ainda aparece como pendente. O que faço? | Recuperar o trecho sobre pagamentos pendentes e orientar com base nele, sem consultar a API. |
| Qual é o prazo para contestar uma transferência internacional? | Manter esse assunto fora dos runbooks e verificar se o copiloto informa que a evidência é insuficiente. |
| Qual é o status do pedido 103? | Consultar a API simulada com o ID 103 e informar o status retornado. |
| Qual é o status do meu pedido? | Pedir o ID do pedido antes de consultar a API. |

Se houver tempo, compare também a busca híbrida, que combina busca textual e vetorial. Use os mesmos casos para verificar se a combinação melhora a recuperação por código exato e por paráfrase.

## Configuração do Ollama

Na etapa de integração, confirme a conectividade pela VPN e os modelos disponíveis para geração e embeddings. Use variáveis de ambiente como `OLLAMA_BASE_URL`, `OLLAMA_CHAT_MODEL` e `OLLAMA_EMBED_MODEL`. Documente exemplos com valores genéricos. Use documentos e pedidos fictícios na demo e mantenha credenciais e endereços privados fora do Git.

## Roteiro para a entrevista

- **Workflow multiagente.** Explique a divisão do trabalho entre os agentes, os pontos de validação e como foi medida a redução no tempo de entrega.
- **Webhooks de pagamento.** Explique como foi diagnosticada a perda de eventos, o papel do limite de requisições e por que Kafka e retentativas com backoff resolveram o problema.
- **Experimento com LangGraph.** Explique a validação de saída, a falha de idioma e que evidência você buscaria antes de promover o grafo.
- **Diagnóstico de RAG.** Inspecione os trechos recuperados e repita a pergunta entregando o trecho correto ao modelo. Compare as duas saídas para investigar se a falha começou na recuperação ou na geração.

## Referências

- [Tutorial oficial de Python](https://docs.python.org/3/tutorial/)
- [Primeiros passos com pytest](https://docs.pytest.org/en/stable/getting-started.html)
- [Tutorial do FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [API do Ollama](https://docs.ollama.com/api/introduction)
- [Saída estruturada no Ollama](https://docs.ollama.com/capabilities/structured-outputs)
