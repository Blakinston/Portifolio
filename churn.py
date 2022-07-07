# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn 
import os 

# %%
os.chdir(r'C:\Users\Familia\Documents\Projetos')


# %%
df = pd.read_csv('Src/Compras.txt' ,sep="\t",names=['cliente_id','valor_compra','data_compra'])
df.head()

# %%
df.dtypes

# %%
df.describe

# %%
df.dtypes


# %%
print(df.head())

# %%

df.cliente_id




