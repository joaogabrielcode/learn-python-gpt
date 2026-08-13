# ============================================================
# EXERCÍCIO 05 — Estado de uma entrega
# ============================================================
#
# Enunciado:
#
# Crie variáveis para código do pedido, nome do cliente, status
# da entrega e se o pagamento foi confirmado. Exiba o estado
# inicial. Depois, atribua novos valores ao status e à
# confirmação de pagamento e exiba o estado atualizado.
#
# Regras:
#
# Combine entradas e conversões sem antecipar operadores ou
# decisões.
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
# CONCEITOS PRATICADOS:
#
# - print()
# - variáveis
# - atribuição
# - reatribuição
# - str
# - bool
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