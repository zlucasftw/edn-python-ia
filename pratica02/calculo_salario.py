"""
Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora.
Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:
O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:


Número do funcionário (numero_funcionario).
Quantidade de horas trabalhadas (horas_trabalhadas).
Valor recebido por hora (valor_por_hora).

Saída:
Imprima o número do funcionário e o salário calculado com duas casas decimais.
Deve haver um espaço em branco antes e depois do sinal de igualdade, e no caso do salário,
também um espaço em branco após o R$
"""

# Cálculo do Salário

# Ler valores informados pelo usuário
numero_funcionario = int(input("Insira o número do funcionário: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Insira o valor das horas trabalhadas: "))

# Cálculo do Salário
salario = horas_trabalhadas * valor_por_hora

# Exibição
print(f"""
Número do funcionário: {numero_funcionario}
Salário = R$ {salario}
""")
