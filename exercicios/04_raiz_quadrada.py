# 4) Faça um programa que receba um número inteiro e calcule sua raiz quadrada e 
# exiba o resultado

numero = int(input("Digite um número inteiro para calcular a sua raiz quadrada: "))

raiz = round(numero ** (1/2), 2)  # numero ** 0.5

print("A raiz quadrada de", numero, "é", raiz)