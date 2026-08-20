# ============================================================
# EXERCÍCIO 13 — Média ponderada
# ============================================================
#
# Enunciado:
#
# Leia três notas com pesos 2, 3 e 5. Calcule a média ponderada
# e exiba-a com uma casa decimal.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# 7
# 8
# 9
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Média ponderada: 8.3
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Montar uma expressão respeitando pesos e precedência.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - operadores aritméticos
# - precedência
# - média ponderada
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

print("### CALCULADORA DE MEDIA PONDERADA ###")
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))

calculo_media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"Media Ponderada: {calculo_media:.1f}")