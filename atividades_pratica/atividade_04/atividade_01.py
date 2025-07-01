"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas
(adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve
ser capaz de lidar com diversos tipos de erros de entrada e operação.
Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma
operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e /
(divisão).

O programa deve continuar solicitando entradas até que uma operação válida
seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar
nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre
o programa.
"""

while True:
    try:
        numero_01 = float(input("Digite o primeiro número: "))
        numero_02 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação que deseja (+, -, *, /): ")

        operacoes = ["+", "-", "*", "/"]
        resultado = 0

        if operacao not in operacoes:
            raise ValueError("Operação inválida!")

        if operacao in operacoes[0]:
            resultado = numero_01 + numero_02
        elif operacao in operacoes[1]:
            resultado = numero_01 - numero_02
        elif operacao in operacoes[2]:
            resultado = numero_01 * numero_02
        elif operacao in operacoes[3]:
            resultado = numero_01 / numero_02

        print(f"Resultado da operação de {numero_01:.2f} {operacao} {numero_02:.2f} = {resultado:.2f}")

        break

    except ValueError as erro:
        print(f"Erro: {erro}\nTente novamente!")
    except ZeroDivisionError:
        print("Não é possível dividir por zero. Tente novamente!")