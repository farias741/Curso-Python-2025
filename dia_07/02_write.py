# %%

# Como escrever um texto no python

txt = "Meu novo arquivo\n"
nome_arquivo = "historia_02.txt"

# mode = se você quer ler em formato de leitura que vai ser
# "r" que default(padrão)
# ou de escrita que vai ser "w"

with open(nome_arquivo, mode="w") as open_file: # escrevendo um arquivo
    open_file.write(txt)

# %%

# Adicionar coisas novas

txt = "Esqueci o nome do arquivo\n" # \n é quebra de linhas
nome_arquivo = "historia_02.txt"


with open(nome_arquivo, mode="a") as open_file: # Adicionar caracteres novos
    open_file.write(txt)
