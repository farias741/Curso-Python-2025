# Faça um programa que receba um número.
#  Verifique se o número informado é par ou ímpar.
#  Exiba o resultado da seguinte maneira

# O número x é impar ou O número x é par

def par_impar(numero:int):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = input("Entre com um número: ")
numero = int(numero)

resultado = par_impar(numero)

print("O valor", numero, "é", resultado)