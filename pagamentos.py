class EventoPagamento:
  def __init__(self, pedido_id, status=None):
    self.pedido_id = pedido_id
    self.status = status
eventos = [
    EventoPagamento(1,"paid"),
    EventoPagamento(2,"failed"),
    EventoPagamento(3,None),
    EventoPagamento(4,"refunded")
]
def decidir_acao(evento):
  status = evento.status
  if(status == "paid"):
    return "confirmar_pedido"
  elif(status == "failed"):
    return "registrar_falha"
  elif(status == "refunded"):
    return "registrar_estorno"
  else:
     return "ignorar"

for event in eventos:
   acao = decidir_acao(event)
   print(f"{event.pedido_id}: {acao}")
