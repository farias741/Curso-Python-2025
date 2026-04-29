# Altere o programa anterior para considerar
#  a quantidade de garrafas de água

texto = """
Escolha a sua água para comprar
(1) Água mineral natural - 1,50
(2) Água mineral com gás - 2,50

"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item  == 0:
    print("Entre com a opção correta, por favor.")

else: 
    qtde = input("Quantas garrafas? ")
    qtde = int (qtde)
    valor_item = valor_item * qtde
    print("Sua conta é R$", valor_item)
    