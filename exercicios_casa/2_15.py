# %%

# Escreva um programa que receba uma lista 
# de números do usuário e conte quantas
#  vezes um número específico aparece na lista. Solicite ao 
# usuário um número e exiba a contagem

lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

# Entra com numero
numero = input("Entre com um número: ")
numero = int(numero)

contador = 0 # inicio, contar de zero, antes
# de pecorrer a lista

# ex: a pessoa colocou o número 1, 
# começou em zero
# entro no for da lista i passa a valer 1
for i in lista:
    # 1 é igual o numero que foi digitado 
    if i == numero:
    # se for, vou pegar o meu contador e vou
    # adicionar 1, e assim sucessivamente
        contador += 1

print("Quantidade de", numero, ":", contador)



