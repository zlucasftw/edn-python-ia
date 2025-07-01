"""
Enunciado: Crie uma função que calcule a gorjeta a ser deixada em
um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada.

Calcula o valor da gorjeta baseado no total da conta e na
porcentagem desejada.

Parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna:
float: O valor da gorjeta calculada
"""

def calcula_gorjeta(valor_conta, porcentagem_gorjeta):
    return (valor_conta / 100) * porcentagem_gorjeta


total = 100
porcentagem = 10

print(f"O valor da gorjeta para o valor total R$ {total:.2f} é de R$ {calcula_gorjeta(total, porcentagem):.2f}")
