"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em
relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda
desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última atualização. Utilize a API da
AwesomeAPI para obter os dados de cotação.
"""
import datetime

import requests

def consulta_cotacao(codigo_moeda : str):

    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"

    try:

        resultado = requests.get(url)
        resultado.raise_for_status()

        json = resultado.json()

        resultado_json = {
            "valor_atual": json["low"],
            "maximo": json["high"],
            "ultima_atualizacao": datetime.datetime.fromtimestamp(json["timestamp"])
        }


    except requests.HTTPError:
        print("Erro ao realizar a requisição")
        return ""



try:
    moeda_desejada = input("Digite o código da moeda desejada (USD, EUR, GBP): ")

    if moeda_desejada not in ["USD", "EUR", "GBP"]:
        raise ValueError

    print(f"Cotação atual da moeda {moeda_desejada}")

    valor_convertido = consulta_cotacao(moeda_desejada)
    print(f"Valor atual: {}")

except ValueError:
    print("Entrada de código inválida!")