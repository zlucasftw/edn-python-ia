"""
2- Calculadora de Desconto

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20%

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_de_desconto = 20

valor_do_desconto = ((preco_original / 100) * porcentagem_de_desconto)

valor_final = preco_original - valor_do_desconto

print(f"Nome do produto: {nome_do_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_de_desconto}%")
print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço final: R$ {valor_final:.2f}")
