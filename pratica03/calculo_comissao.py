"""
Faça um programa que leia o nome de um vendedor,
o seu salário fixo e o
total de vendas
efetuadas por ele no mês (em dinheiro).

Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
informar o total a receber no final do mês, com duas casas decimais.

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor)
e 2 valores de dupla precisão (double) com duas casas decimais,
representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente.

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

# Solicitando o nome do vendedor
nome = input("Favor inserir o nome do vendedor: ")

# Solicitar salário fixo e total de vendas no mês
salario_fixo = float(input("Insira o salário fixo: R$ "))
total_vendas = float(input("Insira o total de vendas: R$ "))

# Cálculo da Comissão
comissao_percentual = 0.15
comissao = total_vendas * comissao_percentual

# Cálculo do total a receber
total_receber = salario_fixo + comissao

# Exibição para o usuário
print(f"O vendedor {nome} irá receber R$ {total_receber:.2f}")
