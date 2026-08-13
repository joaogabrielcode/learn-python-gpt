# ============================================================
# EXERCÍCIO 04 — Troca de valores
# ============================================================
#
# Enunciado:
#
# Crie duas variáveis com nomes de cidades, mostre-as, troque
# seus valores e mostre o resultado sem perder nenhuma cidade.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# sem entrada
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Antes: Recife, Natal
# Depois: Natal, Recife
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Preservar um dado durante a reatribuição de variáveis.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - atribuição
# - reatribuição
# - variável temporária
# - print()
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:


cidade = "Natal"
cidade2 = "Recife"
temp = ""

print("Antes: ", cidade, cidade2)

temp = cidade2
cidade2 = cidade
cidade = temp

print("Depois: ", cidade, cidade2)
