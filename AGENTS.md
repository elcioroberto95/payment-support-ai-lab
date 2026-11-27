# Contexto do projeto

Este laboratório ensina Python e Engenharia de IA por meio de um copiloto de suporte a pagamentos. O objetivo é preparar uma demo para a entrevista de **09/12/2026**. Consulte o [README.md](README.md) para acompanhar as aulas, as prioridades e os critérios de conclusão.

## Cenário da demo

Um pedido continua pendente. O copiloto usa runbooks fictícios para orientar o suporte e cita o documento e a seção ou página. Se precisa confirmar o status de um pedido específico, consulta uma API simulada de somente leitura. Se falta o ID, pede esse dado. Se os runbooks não sustentam uma resposta, informa que não encontrou evidência suficiente.

## Como ajudar neste repositório

- Responda em português do Brasil e adapte a explicação ao nível da aula. Em exercícios de aprendizagem, dê uma pista ou um exemplo pequeno e deixe a implementação com o usuário, salvo quando ele pedir a solução.
- Na branch `aula/01-python`, comece com `pagamentos.py`. Pratique listas, dicionários, condicionais e funções. Em seguida, teste `decidir_acao(evento)` com pytest e avance para leitura de JSON. Use os comandos do README no PowerShell.
- Ensine POO a partir da Aula 3. Use `EventoPagamento` para praticar `class`, instâncias, `__init__`, `self`, atributos e métodos. Retome classes com os modelos Pydantic e com o cliente Ollama. Preserve a função de decisão e seus testes.
- Reaproveite a regra de pagamentos na etapa de FastAPI. Na integração com Ollama, use Pydantic para gerar o schema e validar a saída estruturada. Configure URL e modelos por variáveis de ambiente.
- Use pedidos, relatos e runbooks fictícios. Mantenha credenciais e endereços privados fora do Git.
- No RAG, preserve a referência de origem dos trechos. Use os casos do README para medir recuperação, fidelidade à fonte, validade do JSON, roteamento e latência. Registre o suficiente para investigar falhas de recuperação, geração e consulta de status.
- Priorize o fluxo simples da demo. Busca híbrida, pgvector, MCP e LangGraph são extensões se houver tempo.
