# ============================================================
# EXERCÍCIO 06 — Validação e campo calculado
# ============================================================
#
# Enunciado:
#
# Modele ItemPedido como dataclass, valide quantidade e preço em
# __post_init__ e ofereça total calculado sem armazenar valor
# redundante.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# Livro 2 40
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Total: 80.00
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Combinar dataclass com invariantes e valor derivado.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - __post_init__
# - property
# - ValueError
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

