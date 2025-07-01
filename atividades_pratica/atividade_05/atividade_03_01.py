"""
Crie um programa que receba o preço original de um produto e um percentual de
desconto, realizando o cálculo do preço final após a aplicação do desconto.

Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.

Utilizar operações matemáticas para calcular o valor do desconto e o preço
final.

Exibir o preço final com duas casas decimais para garantir precisão. Entrada
esperada: preço do produto (exemplo: 250.75) e o percentual de desconto
(exemplo: 10).
"""

def calcula_preco_final(preco_original : float, percentual_desconto : float):
    return preco_original - ((preco_original / 100) * percentual_desconto)


try:

    preco_produto = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o percentual de desconto: "))

    print(f"Preço final é de: R$ {calcula_preco_final(preco_produto, desconto):.2f}")

except ValueError:
    print("Digite um valor numérico!")