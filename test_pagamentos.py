import pytest
from pagamentos import decidir_acao,EventoPagamento
@pytest.mark.parametrize (
    "evento, acao_esperada",
    [
        (EventoPagamento(1,"paid"),"confirmar_pedido"),
        (EventoPagamento(2,"failed"),"registrar_falha"),
        (EventoPagamento(3,"refunded"),"registrar_estorno"),
        (EventoPagamento(4,None),"ignorar"),
    ]
)
def test_decidir_acao(evento, acao_esperada):
    resultado = decidir_acao(evento)
    assert resultado == acao_esperada