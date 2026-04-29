# %%

# Escreva um programa que solicite ao usuário um nome e uma idade,
#  e crie um dicionário com essas informações. 
# Em seguida, exiba o dicionário.

# Dados do usuário

nome = input("Entre com o nome: ")
idade = int(input("Entre com a idade: "))

# Criar dicionário

pessoa = {"nome": nome,
      "idade": idade}

print("Exibindo o dicionário: ", pessoa)
