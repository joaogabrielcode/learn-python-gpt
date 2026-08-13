# ============================================================
# EXERCÍCIO 05 — Estado de uma entrega
# ============================================================
#
# Enunciado:
#
# Represente código do pedido, cliente, status e confirmação do
# pagamento. Exiba o estado inicial, atualize status e pagamento
# e exiba o novo estado claramente separado.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# sem entrada
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Pedido: PED-104
# Cliente: Lia
# Status: aguardando pagamento
# Pagamento confirmado: False
#
# Estado atualizado
# Status: preparando envio
# Pagamento confirmado: True
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Representar uma mudança de estado por reatribuição.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - variáveis
# - reatribuição
# - str
# - bool
# - f-strings
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:
codigo_pedido = "PED-134"
nome_cliente = "João Gabriel"
status_pedido = "Aguardando pagamento"
pagamento = False

print("Pedido: ", codigo_pedido)
print("Nome do Cliente: ", nome_cliente)
print("Status do Pedido: ", status_pedido)
print("Pagamento confirmado: ", pagamento)

statusPedido = "Pagamento Aprovado com sucesso"
pagamento = True

print("### Pedido Atualizado ###")

print("Status do Pedido: ", statusPedido)
print("Pagamento confirmado: ", pagamento)
