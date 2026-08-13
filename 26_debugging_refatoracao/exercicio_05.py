# ============================================================
# EXERCÍCIO 05 — Estado mutável compartilhado
# ============================================================
#
# Enunciado:
#
# A função abaixo reutiliza a mesma lista entre chamadas que deveriam
# ser independentes. Escreva um teste que reproduza o defeito,
# investigue quando o argumento padrão é criado e refatore a função
# para produzir listas independentes.
#
# CÓDIGO PARA INVESTIGAR:
#
# def adicionar(nome, nomes=[]):
#     nomes.append(nome)
#     return nomes
#
# Regras:
#
# Combine o assunto atual com os fundamentos já praticados.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# adicionar Ana; nova lista com Bia
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# ['Ana']
# ['Bia']
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - argumento padrão mutável
# - estado compartilhado
# - None como sentinela
# - teste de regressão
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:
