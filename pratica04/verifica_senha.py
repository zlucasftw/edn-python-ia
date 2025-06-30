"""
Crie um programa que verifique se uma senha é forte.
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""

# A entrada da senha
def verifica_senha():
    while True:
        senha = input("Digite uma senha (ou digite 'sair' para encerrar): ")

        # Verificação do comando 'sair'
        if senha.lower() == 'sair':
            print("O programa foi encerrado.")
            break

        # Verificação do comprimento da senha
        if len(senha) < 8:
            print("Senha fraca. A senha deve precisa ter pelo menos 8 caracteres.")
            continue

        # Verificação de presença de pelo menos 1 número
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca. A senha precisa ter pelo menos um número.")
            continue

        # Verificação de presença de pelo menos 1 letra
        if not any(caractere.isAlpha() for caractere in senha):
            print("Senha fraca. A senha precisa ter pelo menos uma letra.")
            continue

        # Verificação de presença de pelo menos 1 letra maiúscula
        if not any(caractere.isupper() for caractere in senha):
            print("Senha fraca. A senha precisa ter pelo menos uma letra maiúscula.")
            continue

        # Se chegar até aqui deu tudo certo!
        print("A senha é forte!")
        break


verifica_senha()