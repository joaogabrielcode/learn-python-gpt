# ============================================================
# EXERCÍCIO 06 — Uma variável, tipos diferentes
# ============================================================
#
# Enunciado:
#
# Crie uma variável chamada dado. Atribua a ela, em momentos
# diferentes, um texto, um número inteiro, um decimal e um valor
# lógico. Após cada atribuição, mostre o valor e seu tipo.
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
# Python — <class 'str'>
# 30 — <class 'int'>
# 1.75 — <class 'float'>
# True — <class 'bool'>
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - print()
# - variáveis
# - reatribuição
# - type()
# - tipagem dinâmica
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:
dado = "Python"
print(dado, type(dado))

dado = 30
print(dado, type(dado))

dado = 1.75
print(dado, type(dado))

dado = True
print(dado, type(dado))