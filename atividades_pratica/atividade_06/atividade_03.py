"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP
fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro,
bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consulta_cep(cep : str):
    cep = (cep.replace(" ", "")
           .replace("-", "")
           .replace(".", "")
           .strip())

    if len(cep) < 8:
        raise ValueError("CEP inválido!")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:

        # Realiza requisição da URL fornecida
        resultado = requests.get(url)
        resultado.raise_for_status()
        json = resultado.json()

        if json['erro']:
            raise ValueError("CEP inválido!")

        resultado = {
            "logradouro": json["logradouro"],
            "bairro": json["bairro"],
            "cidade": json["localidade"],
            "estado": json["estado"]
        }

        return resultado

    except requests.HTTPError as erro:
        print(f"Erro na requisição: {erro}")
    except ValueError as erro:
        print(f"Erro no CEP digitado: {erro}")



cep_requisicao = input("Digite o CEP que deseja consultar: ")
endereco = consulta_cep(cep_requisicao)

print(f"""
Logradouro: {endereco["logradouro"]} 
Bairro: {endereco["bairro"]} 
Cidade: {endereco["cidade"]} 
Estado: {endereco["estado"]} 
""")

