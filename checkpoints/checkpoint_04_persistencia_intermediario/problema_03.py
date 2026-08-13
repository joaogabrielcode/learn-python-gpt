# ============================================================
# CHECKPOINT — PROBLEMA 03 — Analisador de logs
# ============================================================
#
# Enunciado:
#
# Processe log grande linha a linha, valide timestamps e níveis,
# conte padrões e produza as primeiras ocorrências de cada erro
# sem carregar tudo em memória.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# aplicacao.log
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# INFO: 300
# WARNING: 20
# ERROR: 5
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Projetar pipeline preguiçoso com tratamento por registro.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - yield
# - datetime textual
# - exceptions
# - dicionários
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

