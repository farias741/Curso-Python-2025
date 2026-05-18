# %%

# Importando Biblioteca

import requests
import pandas as pd

# Api

url = "https://api.opendota.com/api/heroes"

resp = requests.get(url)

df = pd.DataFrame(resp.json())

# %%

# Salvar
df.to_csv("heroes_dota.csv", sep=";", index=False)