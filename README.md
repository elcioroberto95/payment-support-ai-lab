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

## Roadmap até a entrevista

| Período | Etapa | Critério de conclusão |
| --- | --- | --- |
| 26–29/11 | **Python e pytest** · Funções, listas, dicionários, imports, tipos, leitura de JSON e `try/except`. | Ler eventos de um arquivo JSON, tratar um arquivo inválido e passar os casos de teste da regra de pagamentos. Usar uma fixture quando houver dados compartilhados entre testes. |
| 30/11–01/12 | **FastAPI** · Reaproveitar a regra em `POST /payments/events` com modelos Pydantic para entrada e saída. | Demonstrar um evento válido e uma requisição fora do contrato em testes HTTP. |
| 02/12 | **Ollama pela VPN** · Criar `POST /incidents/classify` e integrar a API do modelo. Configurar endereço e modelo pelo ambiente. | Rodar uma chamada real com um relato fictício e devolver categoria, resumo e próxima ação em JSON validado. Escrever testes com resposta simulada, timeout e saída inválida. |
| 03/12 | **Extração de documentos** · Ler um PDF com texto selecionável e extrair dados de um runbook. | Produzir JSON com código de erro, causa, procedimento e página de origem. Conferir os campos com o PDF. |
| 04–05/12 | **RAG e embeddings** · Dividir três runbooks fictícios em trechos, guardar metadados de origem e buscar por similaridade. | Confirmar um modelo de embeddings no Ollama da VPN, recuperar trechos relevantes e responder citando documento e seção ou página. Se faltar evidência, devolver uma resposta explícita de insuficiência. Começar com busca local e usar PostgreSQL com pgvector se houver tempo. |
| 06/12 | **Evals** · Criar cinco perguntas fixas com fonte e resultado esperados, incluindo paráfrase e pergunta sem resposta. | Comparar busca textual e vetorial com o mesmo modelo e prompt. Registrar recuperação do trecho certo, fidelidade à fonte, validade do JSON e latência. Anotar uma falha e como foi investigada. |
| 07/12 | **Tool calling, MCP e agente** · Criar uma consulta de status de pagamento somente leitura e expô-la por MCP. Usar LangGraph se o fluxo principal estiver pronto. | Demonstrar um caso em que basta o runbook, outro em que é preciso consultar o pedido e um terceiro em que falta o ID. Tratar pedido inexistente e indisponibilidade da ferramenta. |
| 08/12 | **Simulação da entrevista** · Ensaiar a demo e revisar decisões técnicas. | Em cinco minutos, mostrar uma resposta com fonte, uma falha e o teste ou a avaliação que ajuda a explicá-la. |

Se o prazo apertar, priorize **Python, testes, FastAPI, uma chamada real ao Ollama, RAG pequeno e cinco casos de avaliação**. MCP e o agente podem ficar como extensões da demo.

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
