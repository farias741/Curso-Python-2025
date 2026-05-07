# %%

nome_arquivo = "historia.txt"

# Faz a mesma coisa que está abaixo, apenas dois comandos de linha
# o with serve para abrir a leitura do arquivo e atribuir a uma variável
# chamada open_file, onde consegue acessar os recursos desse arquivo aberto

with open(nome_arquivo) as open_file:
    conteudo = open_file.read() # processando os dados

print(conteudo)

# Abre o arquivo em formato de leitura

#open_file = open(nome_arquivo)


# %%

# Lê os dados do arquivo 

#conteudo = open_file.read()
#print(conteudo)

# %%

# Pra garantir que eu possa modificar o arquivo,
# sem corromper o arquivo

# Fecha o arquivo

#open_file.close()