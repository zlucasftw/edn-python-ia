# Calculadora da soma de dois números

# numero  = 5
# texto   = "Esse aqui é um texto"

# print(numero)

try:
    numero01 = int(input("Digite o primeiro número: "))
    numero02 = int(input("Digite o segundo número: "))

    # O cálculo da soma
    soma = numero01 + numero02

    # Exibição dos valores
    print(f"A soma de {numero01} + {numero02} é: {soma}")
except ValueError:
    print("Digite um número!")

