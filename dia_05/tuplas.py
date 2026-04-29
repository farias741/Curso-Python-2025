# %%

# Uma tupla vai ser uma lista imutavel a lista 
# é multavel
 
dados_teo = [32, 1, "Casado", "dev goLang"]
dados_teo

# %%

dados_teo.append("3241.43")
dados_teo
# %%

# Tuplas

# São listas que não podem ser alteradas

# tupla_teo = 32, 1, "Casado", "dev goLang"
tupla_teo = (32, 1, "Casado", "dev goLang", ['maria', 'antonia'])

print(type(tupla_teo))
print(tupla_teo)

# %%

tupla_teo[-1].append("ana")

# %%

tupla_teo

# A tupla é imutavel no sentido que não pode 
# trocar os elementos (adicionar elementos), mas
# se eu tenho dentro da tupla um objeto mutavel
# pode-se adicionar sim elementos que no caso do 
# exemplo acima, temos uma lista dentro da tupla