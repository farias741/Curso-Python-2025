# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior  ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random

def  get_input():
    while True:
        try: # vai tentar fazer isso
            numero_usuario = int(input("Entre com um número: "))
        
        except ValueError as err:
            print("Valor inválido!")
            continue # simplesmente vai passar para o próximo laço

        if 1 <= numero_usuario <= 15:
            return numero_usuario
        
         
        print("Valor inválido! O valor deve ser entre 1 e 15")
         #if numero_usuario >15 or nuemro_usuario <1:
         #if 1 > numero_usuario or numero_usuario > 15:


def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print("Parabéns! Você se tornou um milionário")
        return True # acertou
    
    elif usuario > sorteio:
         print("Número muito alto. Tente um número menor!")
         return False # errou

    else:
        print("Número muito baixo. Tente um número maior!")
        return False # errou

numero_sorteio = random.randint(1,15)

for i in range(3):
    
    numero_usuario = get_input()

    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario): #check_numbers vai um True ou um False
        break


else:
    print("Suas tentativas acabaram!!")