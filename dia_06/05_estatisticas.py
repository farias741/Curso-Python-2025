# *args -> um conjunto de elementos, onde isso vira uma lista ou uma tupla, absorve varios valores e sempre é colocado no final
# obs: a e b tem que ser obrigatorio

def soma(a:float, b:float, *args)->float:
    valores =  [a,b] + list(args)
    return sum(valores)


def media(a:float, b:float, *args)->float:
    return soma(a,b, *args) / (len(args)+2)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))

print("Média:", media(a,b,c,d))
