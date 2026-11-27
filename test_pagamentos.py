import pytest
from pagamentos import decidir_acao
@pytest.mark.parametrize (
    "evento, acao_esperada",
    [
        ({"status":"paid"},"confirmar_pedido"),
        ({"status":"failed"},"registrar_falha"),
        ({"status":"refunded"},"registrar_estorno"),
        ({"status":"pending"},"ignorar"),
        ({},"ignorar")
    ]
)
def test_decidir_acao(evento, acao_esperada):
    resultado = decidir_acao(evento)
    assert resultado == acao_esperada