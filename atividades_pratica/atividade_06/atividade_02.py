"""
Crie um programa que gera um perfil de usuário aleatório
usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado.
"""

import requests

def gera_usuario_aleatorio():
    try:

        url = "https://randomuser.me/api/"
        usuario = requests.get(url)

        if usuario.status_code == 200:
            usuario = usuario.json()['results'][0]
            resultado = {
                "nome": f"{usuario['name']['first']} {usuario['name']['last']}",
                "email": f"{usuario['email']}",
                "pais": f"{usuario['location']['country']}"
            }
            return resultado
        else:
            raise requests.RequestException("Erro na requisição HTTP")

    except requests.RequestException as erro:
        print(f"Erro: {erro}")



usuario_gerado = gera_usuario_aleatorio()
print(usuario_gerado)
print(f"Nome: {usuario_gerado['nome']}\nE-mail: {usuario_gerado['email']}\nPaís: {usuario_gerado['pais']}")
