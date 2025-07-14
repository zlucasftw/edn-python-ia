"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine
Learning. Calcule a média e o desvio padrão do tempo de execução constantes.
"""

import pandas as pd

def ler_arquivo(nome_arquivo : str, extensao : str):
    try:

        data_frame = pd.read_csv((nome_arquivo + extensao))
        return data_frame

    except FileNotFoundError:
        print("Arquivo não encontrado!")


def calcula_media(dados_arquivo) -> float :
    media = dados_arquivo['tempo_execucao'].mean()
    return media


def calcula_desvio_padrao(dados_arquivo) -> float :
    desvio_padrao = dados_arquivo['tempo_execucao'].std()
    return desvio_padrao


try:
    # Leitura de entrada do usuário para buscar arquivo desejado
    nome_do_arquivo = input("Digite o nome do arquivo de log do dataset de Machine Learning: ")
    extensao_do_arquivo = input("Digite o nome da extensão do arquivo: ")

    # Chamada de funções para processamento e calculo do arquivo
    arquivo = ler_arquivo(nome_do_arquivo, extensao_do_arquivo)
    media_tempo = calcula_media(dados_arquivo=arquivo)
    desvio_padrao_tempo = calcula_desvio_padrao(dados_arquivo=arquivo)

    # Mostra resultado do processamento no terminal para o usuário
    print(f"A média do tempo de execução do treinamento do Modelo de Machine Learning foi: {media_tempo:.2f} segundos")
    print(f"O desvio padrão do tempo de execução do treinamento do Modelo de Machine Learning é de: {desvio_padrao_tempo:.2f} segundos")

except (ValueError, KeyError):
    print("Digite o nome do arquivo correto!")
except Exception as erro:
    print("Erro inesperado no processamento dos arquivos de logs.")
    print(f"Erro: {erro}")
