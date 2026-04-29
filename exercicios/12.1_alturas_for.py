# %%

# Faça um programa que receba 4 alturas usando um laço de repetição e realize a 
# soma dessas alturas.

soma = 0           # valor final
qtde_entradas = 4   # o contador de entrada

for i in range(qtde_entradas): # reange(0, qtde_entradas)
    altura = float(input("Entre com a altura: "))
    # altura = float(altura)
    soma += altura

print("A soma das alturas:", soma)