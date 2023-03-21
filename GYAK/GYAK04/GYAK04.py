# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt ami a bemeneti dictionary-ből egy DataFrame-et ad vissza.

Egy példa a bemenetre: test_dict
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: dict_to_dataframe
'''

# %%
stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

# %%
def dict_to_dataframe(datas: dict)->pd.DataFrame:
    df = pd.DataFrame(datas)
    return df
df = dict_to_dataframe(stats)
df.head()

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyező.

Egy példa a bemenetre: test_df, 'area'
Egy példa a kimenetre: test_df
return type: pandas.core.series.Series
függvény neve: get_column
'''

# %%
def get_column(datas: pd.DataFrame,column_name: str)->pd.Series:
    copy_datas = pd.DataFrame.copy(datas)
    return copy_datas[column_name]
df = dict_to_dataframe(stats)
get_column(df,"capital")

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja a két legnagyobb területű országhoz tartozó sorokat.

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: get_top_two
'''

# %%
def get_top_two(datas: pd.DataFrame)->pd.DataFrame:
    copy_datas = pd.DataFrame.copy(datas)
    return copy_datas.sort_values(by=["population"], ascending=False).head(2)
df = dict_to_dataframe(stats)
get_top_two(df)

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből kiszámolja az országok népsűrűségét és eltárolja az eredményt egy új oszlopba ('density').
(density = population / area)

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: population_density
'''

# %%
def population_density(datas: pd.DataFrame)->pd.DataFrame:
    copy_datas = pd.DataFrame.copy(datas)
    copy_datas["density"] = copy_datas["population"] / copy_datas["area"] 
    return copy_datas
df = dict_to_dataframe(stats)
population_density(df)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlopdiagramot (bar plot),
ami vizualizálja az országok népességét.

Az oszlopdiagram címe legyen: 'Population of Countries'
Az x tengely címe legyen: 'Country'
Az y tengely címe legyen: 'Population (millions)'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_population
'''

# %%
def plot_population(datas: pd.DataFrame)->plt.figure:
    copy_datas = pd.DataFrame.copy(datas)
    x = copy_datas["country"]
    y = copy_datas["population"]
    plt.xlabel("Country")
    plt.xlabel("Population (millions)")
    plt.title("Population of Countries")

    plt.bar(x, y)
    plt.show()
df = dict_to_dataframe(stats)
plot_population(df)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja az országok területét. Minden körcikknek legyen egy címe, ami az ország neve.

Az kördiagram címe legyen: 'Area of Countries'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_area
'''

# %%
def plot_area(datas: pd.DataFrame)->plt.figure:
    copy_datas = pd.DataFrame.copy(datas)
    plt.title("Area of Countries")
    plt.pie(copy_datas["area"],labels=copy_datas["country"])
    plt.show()
df = dict_to_dataframe(stats)
plot_area(df)


