"""
Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória.
"""

import random


try:

    # Entrada da quantidade de caracteres do usuário
    quantidade = int(input("Digite a quantidade de caracteres da senha: "))

    lista_caracteres = []
    senha = ""

    for _ in range(quantidade):
        lista_caracteres.append(chr(random.randint(33, 127)))

    senha = senha.join(lista_caracteres)

    print(f"A senha aleatória gerada é {senha}")

except ValueError:
    print("Digite um número inteiro!")
