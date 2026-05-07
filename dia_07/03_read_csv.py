# %%

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines() # leitura em lista

#print(lines)

# sendo uma lista, podemos percorrer ela usando o for

for l in lines:
    print(l)

# %%

# Criando um dicionário

# Retirando o \n e o ;

chaves =  lines[0]
chaves

# %%

dados = dict() # criando um dicionário vazio

# Definindo as chaves do arquivo

chaves = lines[0].strip("\n").split(";") # identifiquei o cabeçalho
for c in chaves: # percorri cada cabeçalho (nome, idade, profissao) 
    dados[c] = [] # atribuindo como chave, dados na posição c igual a uma lista vazia

# %%

# Percorrer as demais linhas do arquivo

# Percorrendo todas as linhas a partir da segunda linha
for l in lines[1:]: # da primeira linha até a última
    
    # removendo \n e quebra os valores em uma lista
    valores = l.strip("\n").split(";")

    # (indice e não o valor) i vai valer 0, depois 1 e depois 2
    # "Teo, 32, streamer (0,1,2)"
    for i in range(len(valores)):

        # chaves são nome, idade, profissao
        # chaves na posição 0 é nome
        # na posição idade é 1 e na posição 2 é profissao
        #  valores na posição 0 é Teo, na posição 1 é 32 e na posição 2 é streamer,
        # onde a chave nome  = o valor  Teo
        # chave idade = o valor 32
        # chave profissao = valor streamer e assim sucessivamente
        dados[chaves[i]].append(valores[i])



# %%

# Adicionando uma lista

idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/ len(idades)
media
