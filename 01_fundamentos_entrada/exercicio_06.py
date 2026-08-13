# ============================================================
# EXERCÍCIO 06 — Uma variável, tipos diferentes
# ============================================================
#
# Enunciado:
#
# Use uma única variável chamada dado. Atribua a ela, em
# momentos diferentes, um texto, um inteiro, um decimal e um
# valor lógico. Mostre valor e tipo após cada atribuição.
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
# NOVIDADE CENTRAL:
#
# Observar a tipagem dinâmica ao reutilizar uma variável.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
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
