#%%
import pandas as pd
import seaborn as sns

# %%
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# %%
iris.head()
# %%
iris.describe()
# %%
type(iris)
# %%
iris.dtypes
# %%
iris.columns
# %%