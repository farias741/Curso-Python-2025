# %%

# install pip requests

import requests 

# %%

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "19060100",
    "58038200",
]

# %%

url = "https://viacep.com.br/ws/{cep}/json/"

# %%

dados = []
for i in ceps:
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

# Consumir um dado de uma api(utilizamos o get)

resposta = requests.get(url) # quando queremos obter alguma informação na internet


# %% 

resposta # response [200] significa que a resposta ok, onde a resposta foi aceita(sucesso)

# %%

# Assim é uma string

resposta.text # mostrando o texto da resposta

# %%

# Assim é um dicionário (json)
dados = resposta.json()
dados

# %%

type(dados)

