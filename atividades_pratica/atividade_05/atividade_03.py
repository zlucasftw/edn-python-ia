"""
Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'.
"""

def verifica_senha():
    while True:

        senha = input("Digite uma senha ou digite 'sair' para encerrar o programa: ")

        if senha.lower() == "sair":
            break

        if len(senha) >= 8 and any(letra.isdigit() for letra in senha):
            print("Senha válida forte inserida!")
            break
        else:
            print("Digite uma senha com pelo menos 8 caracteres e pelo menos um número!")


verifica_senha()
