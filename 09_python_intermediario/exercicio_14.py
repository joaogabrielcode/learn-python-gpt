# ============================================================
# EXERCÍCIO 14 — Desafio — Pipeline com generators
# ============================================================
#
# Enunciado:
#
# Leia um arquivo de transações linha a linha. Encadeie
# generators para interpretar, descartar inválidas, filtrar por
# período e produzir totais por categoria sem carregar o arquivo
# inteiro.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# 2026-08-01,alimentação,30
# linha inválida
# 2026-08-02,transporte,20
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# alimentação: 30.00
# transporte: 20.00
# Inválidas: 1
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Organizar processamento preguiçoso em etapas com yield.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - generators
# - yield
# - arquivos
# - pipeline
# - exceptions
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

