# ============================================================
# EXERCÍCIO 09 — Código que preserva zeros
# ============================================================
#
# Enunciado:
#
# Solicite um código numérico que pode começar com zeros e uma
# quantidade. Preserve o código exatamente como digitado e
# converta apenas a quantidade.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# 0075
# 3
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Código: 0075
# Quantidade: 3
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Distinguir identificadores textuais de números usados em
# cálculos.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - input()
# - str
# - int()
# - preservação de formato
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

codigo = input("Digite o codigo: ")
quantidade = int(input("Digite a quantidade: "))

print("Código:", codigo)
print("Quantidade:", quantidade)