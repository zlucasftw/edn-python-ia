"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV
deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import csv

def escrever_csv(nome_arquivo, dados):
    try:

        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            escreve_csv = csv.writer(arquivo_csv)
            escreve_csv.writerow(["Nome", "Idade", "Cidade"])

            for linha in dados:
                escreve_csv.writerow(linha)

        return True
    except FileNotFoundError:
        print("Arquivo não encontrado!")



while True:
    try:
        continuar_execucao =  1
        nome_arquivo_csv = ''
        dados_pessoa = []

        nome_arquivo_csv = input("Digite o nome do arquivo CSV para ser escrito: ")

        while continuar_execucao != 0:


            # Entrada de dados
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            cidade = input("Digite o nome da cidade da pessoa: ")

            dados_pessoa.append([nome, idade, cidade])


            # Pergunta se deseja continuar a execução
            continuar_execucao = int(input("Para continuar a execução digite: 1 ou digite 0 para parar a execução e escrever o arquivo: "))


        # Chama a função para escrita dos dados inseridos
        resultado = escrever_csv(nome_arquivo_csv, dados_pessoa)

        if resultado:
            print(f"Dados salvos em {nome_arquivo_csv}")
        else:
            print(f"Não foi possível salvar os dados em {nome_arquivo_csv}")

        break
    except ValueError:
        print("Erro no tipo de dado de entrada")
    except Exception as erro:
        print("Um erro inesperado ocorreu!")
        print(f"Erro: {erro}")
