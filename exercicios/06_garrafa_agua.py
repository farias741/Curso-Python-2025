# Faça um programa que vende uma garrafa de água:
# a. Se o cliente escolher água mineral natural, será cobrado R$1,50
# b. Se o cliente escolher água mineral com gás, será cobrado R$2,50

 
# string com aspas triplas - multiplas linhas
texto = """
Escolha a sua água para comprar
(1) Água mineral natural 1,50
(2) Água mineral com gás 2,50

"""

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.5
elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Entre com a opcao correta, por favor.")
    
else:
    print("Sua conta é R$", conta)
    