# %%
# Metodos da lista

# 1 - lista vazia
idades = []

# Criou um while
while True:
# 2 - Pediu o input do usuário
    idade = input("Entre com a idade: ")
# 3 - Criou uma condição: se o usuário não colocar
# a idade, interrompe o laço, se colocar a idade
# essa idade vai se adicionada na lista.
    if idade == "":
        break

# Adicionar um elemento novo na lista
# As listas são objetos mutaveis
    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde   = len(idades)

print("MEDIA:", media )
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)