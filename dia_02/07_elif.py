# %%


idade = 20

if idade > 70:
    print("Cuidado com a bebida.")
    print("Consulte seu geriatra!")

# verifica novas condições, se o if anterior for falso.
elif idade >= 18:
    print("Você pode beber cerveja!")
    print("Beba com moderação")

elif idade == 17:
    print("Você ainda não pode beber cerveja!")
    print("Fica no refri!")
else:
    print("Você não pode beber!")
    print("Vá pra casa beber leite!")


