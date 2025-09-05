# %%
import numpy as np
import pandas as pd


# %%
gallup = pd.read_csv('USAIPO1936-0053.csv')

# %%
gallup

# %%
gallup.head(3).T

# %%
pd.crosstab(gallup['Q5A'], gallup['Q3'])

# %% [markdown]
# #KFF Poll

# %%
kff = pd.read_stata('31122600.dta')
pd.set_option('display.max_rows', 164)
kff.head(3).T

# %%
width_data = pd.read_csv('USIA data widths - Sheet1.csv')

# %%
usia = pd.read_fwf('i20068.dat', widths=width_data['Width'], header=None)
usia


