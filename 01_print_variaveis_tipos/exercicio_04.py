# ============================================================
# EXERCÍCIO 04 — Troca de valores
# ============================================================
#
# Enunciado:
#
# Crie duas variáveis com nomes de cidades, mostre-as, troque seus
# valores e mostre o resultado.
#
# Regras:
#
# Considere os dados e regras descritos, inclusive os limites.
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
# CONCEITOS PRATICADOS:
#
# - variáveis
# - atribuição
# - reatribuição
# - variável temporária
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
