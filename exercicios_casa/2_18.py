# Escreva um programa que solicite ao usuário 
# frases. Para parar de solicitar frases, ele pode 
# apenas apertar o “enter”.
# Seu programa deve apresentar cada frase e 
# quantas vezes ela foi repetida.

# criei um dicionario que vai armazenar todas as frases
dados = {} # dicionario vazio

while True:
    frase = input("Entre com a frase: ") # receber uma frase do usuário
    if frase == "": # frase vazia
        break # o programa para

   # se não for fazia, vai verificar se a frase(que está chegando do usuário)
   # ela está dentro dos nossos dados
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

# ordem de mais para menor
items = list (dados.items())
items.sort(key=lambda x: x[-1], reverse=True)


for i,j in items:
    print(i, "->", j)
