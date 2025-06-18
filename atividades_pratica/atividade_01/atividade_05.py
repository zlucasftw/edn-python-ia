# 5- Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
# Entrada: O arquivo de entrada contém 4 valores inteiros.
# Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

try:
    A = int(input("Digite o primeiro número inteiro: "))
    B = int(input("Digite o segundo número inteiro: "))
    C = int(input("Digite o terceiro número inteiro: "))
    D = int(input("Digite o quarto número inteiro: "))

    DIFERENCA = (A * B - C * D)

    print(f"DIFERENCA = {DIFERENCA}")

except ValueError:
    print("Digite um número!")
