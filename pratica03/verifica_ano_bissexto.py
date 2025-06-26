"""
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4,
exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

ano = int(input("Digite um ano: "))

if ano % 4 == 0: # Se for divisível por 4, pode ser que seja bissexto.
    if ano % 100 == 0: # Se for divisível por 100, precisa ser analisado mais uma vez.
        if ano % 400 == 0: # Se for divisível por 400 também, ele é um ano bissexto.
            print(f"{ano} é bissexto.")
        else: # É divisível por 4, por 100, mas não é divisível por 400, portanto não é bissexto.
            print(f"{ano} não é bissexto.")
    else: # É divisível por 4 e não é por 100, portanto é bissexto.
        print(f"{ano} é bissexto.")
else: # Se não for divisivel por 4, então não é bissexto
    print(f"{ano} não é bissexto.")
