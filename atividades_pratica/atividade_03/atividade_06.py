"""
6- Calculadora de Comissão

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro).

Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
informar o total a receber no final do mês, com duas casas decimais.

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente.

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

try:

    TAXA_COMISSAO = 15

    nome_vendedor = input("Digite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo do vendedor: "))
    total_vendas = float(input("Digite o total de vendas efetuadas do vendedor no mês em dinheiro: "))

    total_receber = salario_fixo + (total_vendas * (TAXA_COMISSAO / 100))

    print(f"""
    Nome do vendedor: {nome_vendedor}
    Salário: R$ {salario_fixo:.2f}
    Total de vendas efetuadas no mês: R$ {total_vendas:.2f}
    Total do salário no final do mês: R$ {total_receber:.2f}
    """)

except ValueError:
    print("Tipo de entrada de dado inválida!")
