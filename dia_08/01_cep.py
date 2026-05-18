# %%

# install pip requests

# Importanto bibliotecas

import requests # para realizar requisição na web
import json # para tratar json de listas/dicionários para arquivos json
from tqdm import tqdm # fornece barras de progresso rápidas, acompanha o andamento de tarefas demoradas.

import pandas as pd

# %%

# Colocamos vários ceps

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

# Criamos uma url base que vai navegar no cep
# Api via cep

url = "https://viacep.com.br/ws/{cep}/json/" # {cep} chamado de please rhoades no python - parametrizar

# %%

# Criando uma lista vazia, onde vai armazenar todos os ceps
dados = []

# Navegando em todos os ceps

for i in tqdm(ceps):

 # Obtendo a resposta da request usando do get
    # url.format(cep=i) - estou pegando o valor do cep
    # dentro da da string chamada o url e substituindo por
    #  i(é o cep com estamos interando)
   
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200: # se a resposta deu um status ok
        dados.append(resposta.json()) # transformar em json e adcionar(append) na lista de dados

dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")
               
# %%

print(dados)

# Salvando o arquivo

# Abrindo um arquivo chamado ceps.json em modo de escrita "w"

with open("ceps.json", "w", encoding='utf-8') as open_file:

    # Pegando a biblioteca json utilizando o método dump
    # passando os dados que queremos fazer o dump, o arquivo que
    # vamos fazer a escrita open_file, coloca-se o argumento 
    #  ensure_ascii=False, onde ele ignora o ascii (tabela ascci de caracteres)
    # e o indent=4 para formatar o arquivo e o 4 é referente a ao espaço da indentação
    
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

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

