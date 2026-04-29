# %%

# Lista dentro de lista

lista = [2 , 132, "teo", ["ds", "de", "da"], True]

lista[2]

# %%

# Dicionário: São pares de chave/valor(são sempre dois(duplas)), 
# isso que dizer que temos uma chave ao um valor associado, 
# ou seja, dicionários são conjuntos de pares chave associado 
# ao um valor.
# é mutavel

# Representando os valores no dicionário

# pares de chave/valor

dados_teo = {"sobrenome":"Calvo",  
             "nome":"Téo", # chave é nome/ valor é Téo
             "filhos": True,
             "formacao":["estatística", "bigdata datascience"],
             "Cargo":[
                 {"nome": "ds jr.", "empresa": "tapps"},
                 {"nome": "ds pl.", "empresa": "sas"},
                 {"nome": "ds sr.", "empresa": "boticario"},
                 {"nome": "ds espec.", "empresa": "via varejo"},]
}

print(dados_teo)

# %%

# Acessar um valor de determinado chave no dicionário
# As chaves nos dicionários podem ser de quais 
# tipo: string, inteiro 
# e float(muito raro de usar, evitar)
# para valor pode ser qualquer tipo

dados_teo["nome"]

# %%

# A última formação do Teo

dados_teo["formacao"][-1]

# %%

# O nome da última empresa que Téo trabalhou

print(dados_teo["Cargo"][-1]["empresa"])

# %%

# Adcionar uma chave nova, quando o meu dicionario estar criado

# criar uma chave nova
dados_teo["estado civil"] = "casado"

# %%

print(dados_teo)

# %%

# descobrir os nomes das chaves
# retorna a listas de chaves que podemos acessar

print("Chaves:", dados_teo.keys())

# Acessar o valores no dicionario

print("Valores:", dados_teo.values())

# Acessar chave/valor no dicionario

print("Items:", dados_teo.items())

# %%

# utilizando o for para pecorrer o dicionário
# mostrando a chave

for i in dados_teo:
    print(i)

# %%

# mostrando chave e valor (UMA MANEIRA)

for i  in dados_teo:
    print(i, "->", dados_teo[i])

# %%

# OUTRA MANEIRA

# mostrando chave/valor(os pares)
for item in dados_teo.items():
    print(item)

# %%

for [chave, valor] in dados_teo.items():
    print(chave, "->", valor)
