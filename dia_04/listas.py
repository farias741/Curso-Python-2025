# %%

# Listas são conjuntos de elementos de qualquer tipo
# Elas são objetos mutaveis
# A lista é um molho de chaves
# -> Listas não são array
# -> Podem ser de qualquer elementos
# -> inteiro, float, string, boleano

# Uma maneira de definir listas
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# %%

teo = ["Téo", "Calvo", 32, True, "Casado", 2342.48]
print(teo)

# %%

# Tipo da lista
type(teo)

# %%

# elemento da lista teo, exemplo elemento 3(32)
# indice da lista teo, exemplo índice 2(32)

# Acessar as posições(índice) da lista
# o indice no python começa em 0

# idade
print(teo[2])

# renda
print(teo[5])

# primeiro índice
print(teo[0])

# %%

# Propriedades da lista (Funções)

idades = [28, 42, 43, 35, 39, 28, 38, 42 ,34]

# A soma de todas as idades
print("Soma das idades: ", sum(idades))

# Quantidade de idades
print("Quantidade de idades: ", len(idades))

# A média das idades (soma de todos os elementos e divide pela a quantidade de elemento)
print("Média das idades: ", sum(idades)/len(idades))

# Menor idade
print("Menor idade: ", min(idades))

# Maior idade
print("Maior idade: ", max(idades))

# %%

# Lista dentro de outra lista (5 elementos)
teo = ["Téo Calvo", 
      32, 
      True, 
      "Casado", 
      ["estagiario", "ds jr.", "ds pl", "ds sr.", "head"],
      [1500, 4000, 4550, 6500, 10000],
      ["Ana", "Maria", "Claudia"]]

# Quantos elementos na lista teo
print(len(teo))

# lista das exs namoradas da lista teo (índice)
print("Índice das exs namoradas: ", teo[6])

# Primeira exs
teo[6][0]

# Ou fazer dessa forma
exs = teo[6]
primeira_ex = exs[0]
print(primeira_ex)

# %%

# Descobrir as exs de uma forma automatica
# Última ex-namorada

tamanho = len(teo)
pos = tamanho - 1
exs = teo[pos]

teo[pos][len(exs)-1]

# %%
# -1 é o último elemento da lista
# ultimo elemento da lista são as exs e a última ex
teo[-1][-1]

# penultimo elemento da ex
teo[-1][-2]

# %%
# Fatiamento: acessar mais de um valor

# Pegar os 4 primeiros elementos

teo[0:4]

# ou

teo[:4]

# As 2 últimas posições de trabalho do teo
# é como se fosse 5-3 = 2
teo[4][3:5]

# ou
teo[4][3:]

# %%
# ou
# colocando -2:  estamos dizendo que queremos elemento 2
# até o fim da lista
teo[4][-2:]

# %%
# teo[ start : stop ]
# na lista é chamado de start : stop (da onde eu começo e da onde eu termino)
# se você ocultar o start, ele vai entender que você está começando
# do inicio da lista, e se você ocultar o stop, ele vai entender que você vai
# até o final da lista.

# %%

# Fazer de trás pra frente
salarios = teo[5]
salarios[::-1] # esse -1 é de trás pra frente
salarios[::2] # pode ser de 2 em 2
# teo[ start : stop : step ] -> começo : fim : como vou navegar de um e um 
# nevegar de trás pra frente, dois e dois