# Faça um programa que verifique se o item que a pessoa escolheu para comprar 
# na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

item = input("Digite o item desejado: ")

lista = ["laranja", "cerveja", "miojo", "carvão", "picanha"]

if item in lista:
    print("O item está disponível na lista da loja!")
else:
    print("O item não está disponível na lista da loja!")


