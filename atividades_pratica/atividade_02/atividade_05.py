"""
5- Calculadora de Soma com Entrada do Usuário

Leia 2 valores inteiros e armazene-os nas variáveis A e B.

Efetue a soma de A e B, atribuindo o seu resultado à variável X.

Entrada: A entrada contém 2 valores inteiros informados pelo usuário.

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.
"""

try:
    # Entrada de números pelo usuário
    A = int(input("Digite o número inteiro A: "))
    B = int(input("Digite o número inteiro B: "))

    # Cálculo da soma
    X = A + B

    # Exibição do resultado na tela
    print(f"X = {X}")

except ValueError:
    # Exibição de mensagem em caso de entrada inválida
    print("Digite um número inteiro")