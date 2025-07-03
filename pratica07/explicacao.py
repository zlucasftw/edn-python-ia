import pandas as pd

dados = {
    "Nome": ["Alice", "Bruno", "Carlos"],
    "Idade": ["25", "35", "22"],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(dados)
print(df)
