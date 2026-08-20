# ============================================================
# EXERCÍCIO 12 — Conta compartilhada
# ============================================================
#
# Enunciado:
#
# Leia o valor da conta, o percentual de gorjeta e a quantidade
# de pessoas. Calcule total com gorjeta e valor por pessoa.
#
# ------------------------------------------------------------
# ENTRADA DE EXEMPLO:
#
# 100
# 10
# 4
#
# ------------------------------------------------------------
# SAÍDA ESPERADA:
#
# Total: 110.00
# Por pessoa: 27.50
#
# ------------------------------------------------------------
# NOVIDADE CENTRAL:
#
# Aplicar percentual antes de dividir um valor.
#
# ------------------------------------------------------------
# CONCEITOS PRATICADOS:
#
# - float()
# - percentuais
# - divisão
# - formatação
#
# ============================================================


# ESCREVA SUA SOLUÇÃO ABAIXO:

valor_conta = float(input("Qual o valor da conta? "))
porcentagem = float(input("Qual a porcentagem da gorgeta? "))
pessoas = int(input("Quantas pessoas? "))

total = (valor_conta * porcentagem / 100) + valor_conta
total_pessoa = total / pessoas

print(f"Total: {total:.2f}")
print(f"Por pessoa: {total_pessoa:.2f}")