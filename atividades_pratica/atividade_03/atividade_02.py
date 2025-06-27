"""
2- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).

"""

try:

    idade = int(input("Digite sua idade: "))

    if idade    >= 60   : print("Idoso")
    elif idade  >= 18   : print("Adulto")
    elif idade  >= 13   : print("Adolescente")
    elif idade  >= 0    : print("Criança")
    else: print("Idade inválida!")

except ValueError:
    print("Digite um número inteiro!")
