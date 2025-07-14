"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo
JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""

import json

def ler_arquivo_json(nome_arquivo):

    dados_lidos_json = []

    try:

        with open(nome_arquivo, 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)
            dados_lidos_json.append(dados_json)

        return dados_lidos_json
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as erro:
        print("Ocorreu um erro inesperado!")
        print(f"Erro: {erro}")



def escrever_arquivo_json(nome_arquivo, dados):

    try:
        with open(nome_arquivo, 'w', newline='') as arquivo_escrita_json:
            json.dump(dados, arquivo_escrita_json)

        print(f"Arquivo escrito com sucesso em: {nome_arquivo}")

    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as erro:
        print("Ocorreu um erro inesperado!")
        print(f"Erro: {erro}")



while True:

    dados_json = []

    try:
        nome_arquivo_json = input("Digite o nome do arquivo com extensão .json: ")

        escolha = 1

        while escolha != 0:

            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            cidade = input("Digite o nome da cidade da pessoa: ")

            dados = {
                "nome": nome,
                "idade": idade,
                "cidade": cidade,
            }

            dados_json.append(dados)

            escolha = int(input("Digite 0 para parar e escrever no arquivo ou 1 para continuar: "))

        escrever_arquivo_json(nome_arquivo_json, dados_json)
        resultado = ler_arquivo_json(nome_arquivo_json)

        if len(resultado) <= 0:
            print("Arquivo sem nenhum dado para ser lido!")

        for dado in resultado:
            print(dado)

        break
    except ValueError:
        print("Valor de entrada inválido!")
    except Exception as erro:
        print("Ocorreu um erro inesperado!")
        print(f"Erro: {erro}")

