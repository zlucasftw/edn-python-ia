"""
1- Conversor de Moeda

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.20

Taxa do euro: R$ 6.15

O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

try:
    TAXA_DOLAR = 5.20
    TAXA_EURO = 6.15

    valor_em_reais = float(input("Digite o valor em reais que deseja converter: "))

    valor_em_euro = valor_em_reais / TAXA_EURO
    valor_em_dolar = valor_em_reais / TAXA_DOLAR

    print(f"Valor em reais: R$ {valor_em_reais:.2f}")
    print(f"Valor em euro: € {valor_em_euro:.2f}")
    print(f"Valor em dolar: $ {valor_em_dolar:.2f}")
except ValueError:
    print("Digite um número!")
