"""
6- Calculadora de salário por horas trabalhadas

Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe
por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:

Número do funcionário (numero_funcionario).

Quantidade de horas trabalhadas (horas_trabalhadas).

Valor recebido por hora (valor_por_hora).

Saída:

Imprima o número do funcionário e o salário calculado com duas casas decimais. Deve
haver um espaço em branco antes e depois do sinal de igualdade, e no caso do salário,
também um espaço em branco após o R$
"""

try:

    # Entrada de dados
    numero_funcionario = int(input("Digite o número do funcionário: "))
    horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
    valor_por_hora = float(input("Digite o valor recebido por hora: "))

    # Cálculo
    salario_funcionario = horas_trabalhadas * valor_por_hora

    # Exibição de saída com as informações
    print(f"\nNúmero do funcionário = {numero_funcionario}")
    print(f"Quantidade de horas trabalhadas = {horas_trabalhadas}")
    print(f"Valor recebido por hora = R$ {valor_por_hora:.2f}")
    print(f"Salário do funcionário = R$ {salario_funcionario:.2f}")

except ValueError:
    # Exibição de mensagem em caso de entrada inválida
    print("Digite apenas números!")
