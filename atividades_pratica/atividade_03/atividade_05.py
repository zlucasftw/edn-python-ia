"""
5- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que
não são divisíveis por 400.
"""

try:

    ano = int(input("Digite um ano: "))

    if ano % 4 == 0 and not (ano % 100 == 0 and not ano % 400 == 0):
        print(f"Ano {ano} é bissexto")
    else:
        print(f"Ano {ano} não é um ano bissexto")

except ValueError:
    print("Digite um número inteiro!")
