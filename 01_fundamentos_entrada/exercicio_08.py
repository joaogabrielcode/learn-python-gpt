# ============================================================
# EXERCÍCIO 08 — Cadastro com conversões
# ============================================================
#
# Enunciado:
#
# Solicite nome, idade e altura. Converta os campos numéricos e
# mostre o tipo armazenado em cada variável.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# Ana
# 25
# 1.68
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Nome: Ana — <class 'str'>
# Idade: 25 — <class 'int'>
# Altura: 1.68 — <class 'float'>
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Escolher e aplicar conversões diferentes em um mesmo registro.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - input()
# - int()
# - float()
# - type()
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
altura = input("Qual sua altura? ")

print(f"Nome: {nome}", type(nome))
print(f"Idade: {idade}", type(idade))
print(f"Altura: {altura}", type(altura))