# =======================================
#  Dataframe Basics
# =======================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
a = pd.Series("a b c d e f g h i j")
print(a)

# =======================================

data = {'Name': ['Jane', 'Jan', 'John', 'Jabin', 'Jace'], 'ID': [
    100, 102, 104, 106, 108], 'Mark': [74, 92, 58, 81, 66]}
frame = pd.DataFrame(data)
# frame
print(frame)

# =======================================

frame_index = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])
# frame_index
print("=======================================")
print(frame_index)

# =======================================


def write_dataframe(ID=None, Mark=None):
    ID = np.arange(1000, 1050, dtype=int)
    Mark = np.random.randint(60, 101, size=50, dtype=int)
    frame_def = pd.DataFrame({'ID': ID, 'Mark': Mark})
    return frame_def


# write_dataframe()
print("=======================================")
print(write_dataframe())

# =======================================

gm = pd.read_table("Data\\gapminder.tsv")
# gm = pd.read_csv("gapminder.tsv", sep = '\t')
# gm
print("=======================================")
print(gm)

# =======================================

# gm.head(7)
print("=======================================")
print(gm.head(7))

# =======================================

# gm.size
print("=======================================")
print(gm.size)

# =======================================

# gm.describe()
print("=======================================")
print(gm.describe())

# =======================================

# gm.dtypes
print("=======================================")
print(gm.dtypes)

# =======================================

# gm.columns
print("=======================================")
print(gm.columns)

# =======================================
#  Subsetting
# =======================================

# gm.iloc[9:19,1]
print("=======================================")
print(gm.iloc[9:19, 1])

# =======================================

# gm.iloc[58:65, 0::2]
print("=======================================")
print(gm.iloc[58:65, 0::2])

# =======================================

# gm.drop([gm.columns[len(gm.columns)-1],gm.columns[len(gm.columns)-2]], axis = 1)
print("=======================================")
print(gm.drop([gm.columns[len(gm.columns)-1],
               gm.columns[len(gm.columns)-2]], axis=1))

# =======================================

gm.rename(columns={'pop': 'Population'}, inplace=True)
gm.set_index('Population')
print(gm)

# =======================================

gm = pd.read_csv("Data\\gapminder.tsv", sep='\t')
gm_nz = gm.loc[gm['country'] == "New Zealand"]
print(gm_nz)

# =======================================

gmnzle = gm_nz.loc[:, "lifeExp"]
print(gmnzle)

# =======================================

print(gm_nz.loc[gm_nz['year'] == 1982, ['pop', 'gdpPercap']])

# =======================================
#  Data Analysis and Visualisation
# =======================================

print("Avg Life Expectancy, Population and GDP per Capita through the years for NZ")
print(gm[['lifeExp', 'pop', 'gdpPercap']].mean())

# =======================================

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
ax1.set
ax1.bar(gm['year'], gm['lifeExp'])
ax2.bar(gm['year'], gm['pop'])
ax3.bar(gm['year'], gm['gdpPercap'])

# =======================================

print("Comparing Japan and NZ, Bigger Life Expectancy is (with continent) :")
gm_jp = gm.loc[gm['country'] == "Japan"]
if gm_nz['lifeExp'].mean() > gm_jp['lifeExp'].mean():
    print(gm_nz['lifeExp'].mean())
    print(gm_nz['continent'].unique())
else:
    print(gm_jp['lifeExp'].mean())
    print(gm_jp['continent'].unique())

# =======================================
#  Adding Columns to the Dataframe
# =======================================

# Max Value
lifeExp_max = gm_nz['lifeExp'].max()
pop_max = gm_nz['pop'].max()
gdpPercap_max = gm_nz['gdpPercap'].max()

# Normalisation
lifeExp_norm = np.divide(gm_nz['lifeExp'], lifeExp_max)
pop_norm = np.divide(gm_nz['pop'], pop_max)
gdpPercap_norm = np.divide(gm_nz['gdpPercap'], gdpPercap_max)

# Developing Factor
devFac = (0.7 * lifeExp_norm + 0.3 * gdpPercap_norm)/pop_norm

# Append and Save
gm_nz['devFac'] = devFac
gm_nz.to_csv('NZ_DataFrame.csv')
print("=======================================")
print(gm_nz)

# =======================================
#  More Visualisation
# =======================================


# =======================================


# =======================================


# =======================================


# =======================================
