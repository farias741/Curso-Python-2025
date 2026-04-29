# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# a. Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# b. Sabor do sorvete: morango, creme, chocolate
# c. Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem 
# cobertura (R$0,00)

sorvete ="""
Escolha do tipo de sorvete
(a1) Casquinha - R$1,00
(a2) Cascão - R$2,50
(a3) Cestinha - R$4,00

"""
opcao = input(sorvete)

nome = 0
if opcao == "a1":
    valor_sorvete = 1.00
elif opcao == "a2":
    valor_sorvete = 2.50
elif opcao == "a3":
    valor_sorvete = 4.00
else:
     print("Entre com a opção correta, por favor.")


sabor = """
(b1) Morango
(b2) Creme
(b3) Chocolate

"""
opcao2 = input(sabor)

if opcao2 == "b1":
    valor_sabor = "Morango"
elif opcao2 == "b2":
    valor_sabor = "Creme"
elif opcao2 == "b3":
    valor_sabor = "Chocolate"
else:
     print("Entre com a opção correta, por favor.")


cobertura = """
(c1) Caramelo - R$1,50
(c2) morango - R$1,50
(c3) chocolate - R$1,50
(c4) sem cobertura - R$0,00

"""

opcao3 = input(cobertura)

valor_cobertura = 0
if opcao3 == "c1":
    valor_cobertura = 1.50
elif opcao3 == "c2":
    valor_cobertura = 1.50
elif opcao3 == "c3":
    valor_cobertura = 1.50
elif opcao3 == "c4":
    valor_cobertura = 0.00
else:
     print("Entre com a opção correta, por favor.")

# Calculo total
total = float(valor_sorvete + valor_cobertura)


# Resumo do pedido
print("\n===== RESUMO DO PEDIDO =====")
print(f"Tipo: {opcao} - R${valor_sorvete:.2f}")
print(f"Sabor: {opcao2}")
print(f"Cobertura: {opcao3} - R${valor_cobertura:.2f}")
print(f"Total a pagar: R${total:.2f}")
print("============================")