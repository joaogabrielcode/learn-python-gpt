# ============================================================
# EXERCÍCIO 10 — Calculadora de consumo
# ============================================================
#
# Enunciado:
#
# Leia a distância percorrida e os litros consumidos. Calcule e
# mostre o consumo médio em quilômetros por litro com duas casas
# decimais.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# 315
# 25
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Consumo médio: 12.60 km/l
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Combinar entrada, conversão, divisão e formatação decimal.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - float()
# - divisão
# - f-strings
# - formatação numérica
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

kilometragem = float(input("Quantos KM percorreu? "))
litros = float(input("Quantos Litros usou? "))

media = kilometragem / litros

print(f"Consumo médio: {media:.2f}")