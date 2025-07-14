"""
Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O
arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""

import csv


def realiza_leitura_csv(nome_arquivo):
    linhas = []
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            arquivo = csv.reader(arquivo_csv)

            for linha in arquivo:
                linhas.append(linha)

        return linhas
    except FileNotFoundError:
        print("Arquivo não encontrado")


try:
    arquivo_entrada = input("Digite o nome do arquivo de extensão .csv para leitura: ")
    resultado = realiza_leitura_csv(arquivo_entrada)

    if len(resultado) <= 0:
        print("Arquivo sem nenhum dado para ser lido!")

    for dado in resultado:
        print(dado)

except ValueError:
    print("Valor de entrada incorreto!")