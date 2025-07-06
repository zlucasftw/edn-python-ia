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

    codigo_moeda += "-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}"

    try:

        resultado = requests.get(url)
        resultado.raise_for_status()

        json = resultado.json()
        json = json[f"{codigo_moeda.replace("-", "")}"]

        resultado_json = {
            "valor_atual": json["bid"],
            "valor_maximo": json["high"],
            "valor_minimo": json["low"],
            "ultima_atualizacao": datetime.datetime.fromtimestamp(int(json["timestamp"]))
        }

        return resultado_json

    except requests.HTTPError:
        print("Erro ao realizar a requisição")
        return "NaN"



try:
    moeda_desejada = input("Digite o código da moeda desejada (USD, EUR, GBP): ")

    if moeda_desejada not in ["USD", "EUR", "GBP"]:
        raise ValueError

    if moeda_desejada == "USD":
        simbolo = "$"
    elif moeda_desejada == "EUR":
        simbolo = ""

    print(f"\nCotação atual da moeda {moeda_desejada}")
    valor_convertido = consulta_cotacao(moeda_desejada)

    print(f"Valor atual: {valor_convertido['valor_atual']}")
    print(f"Valor máximo da cotação: {valor_convertido['valor_maximo']}")
    print(f"Valor minímo da cotação: {valor_convertido['valor_minimo']}")
    print(f"Data e hora da ultima atualização: {valor_convertido['ultima_atualizacao']}")

except ValueError:
    print("Entrada de código inválida!")