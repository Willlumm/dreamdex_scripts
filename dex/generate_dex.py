import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_gen(num):
    gen_nums = [(0, 0), (1, 151), (2, 251), (3, 386), (4, 493), (5, 649), (6, 721), (7, 809), (8, 905), (9, 1008)]
    for gen, num_max in gen_nums:
        if num <= num_max:
            return gen

df = pd.read_json("dex/pokedex.json", orient="index")
# print(df.columns)
# df = df[["num", "name", "types", "genderRatio", "baseStats", "abilities", "heightm", "weightkg", "color", "evos", "eggGroups", "tier", "prevo", "evoLevel", "forme", "gender", "evoItem", "evoCondition", "evoMove", "tags"]]
df = df.join(pd.DataFrame(df.types.tolist(), index=df.index).stack().str.get_dummies().groupby(level=0).sum())
df = df.join(pd.DataFrame(df.eggGroups.tolist(), index=df.index).stack().str.get_dummies().groupby(level=0).sum().add_prefix("eggGroup_"))
df = df.join(pd.json_normalize(df.genderRatio).set_index(df.index))
df = df.join(pd.json_normalize(df.baseStats).set_index(df.index))
df = df.join(pd.json_normalize(df.abilities).set_index(df.index).add_prefix("ability_"))
df = df.join(df["tags"].dropna().apply(lambda x: x[0]).rename("legendary"))
df = df.join(df["evos"].dropna().apply(len).rename("numEvos"))
df.loc[df.gender == "M", ["M", "F"]] = [1, 0]
df.loc[df.gender == "F", ["M", "F"]] = [0, 1]
df.loc[df.gender == "N", ["M", "F"]] = [0, 0]
df["gen"] = df["num"].apply(get_gen)
df.loc[df.forme == "Mega", "gen"] = 6
df.loc[df.forme == "Primal", "gen"] = 6
df.loc[df.forme == "Alola", "gen"] = 7
df.loc[df.forme == "Alola-Totem", "gen"] = 7
df.loc[df.forme == "Galar", "gen"] = 8
df.loc[df.forme == "Gmax", "gen"] = 8
df.loc[df.forme == "Hisui", "gen"] = 8
df.drop(["types", "genderRatio", "baseStats", "abilities", "eggGroups", "gender", "tags", "Bird", "evos"], axis=1, inplace=True)
df.to_csv("dex/pokedex.csv", index=False)
