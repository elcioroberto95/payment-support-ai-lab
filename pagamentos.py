eventos = [
    {"id":1,"status":"paid"},
    {"id":2,"status":"failed"},
    {"id":3},
    {"id":2,"status":"refunded"},
]
def decidir_acao(evento):
  status = evento.get("status")
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
   print(f"{event['id']}: {acao}")
