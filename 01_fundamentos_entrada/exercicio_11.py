# ============================================================
# EXERCÍCIO 11 — Tempo total em segundos
# ============================================================
#
# Enunciado:
#
# Leia horas, minutos e segundos separadamente e calcule a
# duração total em segundos.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# 1
# 2
# 30
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Total: 3750 segundos
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Planejar uma conversão de unidades com operações encadeadas.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - int()
# - multiplicação
# - adição
# - precedência
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

print("CALCULADOR DE HORAS")
horas = int(input("Quantas horas? "))
minutos = int(input("Quantos minutos? "))
segundos = int(input("Quantos segundos? "))

total = (horas * 60) * 60 + minutos * 60 + segundos

print(f"Total: {total} segundos!")
