"""
Crie um programa que solicite ao usuário que insira números inteiros. O programa
deve continuar solicitando números até que o usuário digite 'fim'. Para cada número
inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo
que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de
números pares e ímpares inseridos.
"""

quantidade_par = 0
quantidade_impar = 0

while True:

    try:

        numero = input("Digite um número inteiro ou 'fim' para finalizar a execução: ")

        if numero.lower() == "fim":
            print(f"\nQuantidade de números pares: {quantidade_par}\nQuantidade de números ímpares: {quantidade_impar}")
            break

        numero = int(numero)

        if numero % 2 == 0:
            print(f"O número {numero} é par")
            quantidade_par += 1
        else:
            print(f"O número {numero} é ímpar")
            quantidade_impar += 1

    except ValueError:
        print("Digite um valor de entrada válido!")
