# Faça um programa que receba 4 alturas usando um laço de repetição e realize a 
# soma dessas alturas.

# O while: até quando a condição for verdadeira,
# ou quando não aparecer break no meio.
# é usado em uma condição lógica


soma = 0           # valor final

qtde_entrada = 4   # o contador de entrada

while qtde_entrada > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    qtde_entrada -= 1

print("A soma das alturas:", soma)