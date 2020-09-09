# =======================================
#  Intermediate Practice
# =======================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("https://bit.ly/2purmS1", sep=",")
df.head()

# =======================================

df.dtypes

# =======================================


df["Education"]  # same as df.Education HOWEVER, the dot notation cannot work with spaces

# =======================================


df[["Gender", "Education"]]  # multiple columns need 2 []

# =======================================

df.loc[0:10, "Gender"]
df.iloc[0:10, 1:3]

# =======================================

df.drop(0).head()
df.drop("Gender", axis=1).head()

# =======================================

df2 = pd.read_csv("https://bit.ly/2zopYWO", sep=",")
df2.head()

# =======================================

# contains the word computer in the tags column
df2.tags.str.contains("computer")

# =======================================

df2[df2.tags.str.contains("computer")]

# =======================================

df2[df2.tags.str.contains("computer")].tags.str.contains("Google").sum()
# contains the word computer and Google in the tags column)

# =======================================

# change all the names of the main speakers to upper case
df2.main_speaker.str.upper()

# =======================================

df3 = pd.DataFrame({"A": ["foo", "bar", "foo", "bar",
                          "foo", "bar", "foo", "bar"],
                    "B": ["one", "one", "two", "three",
                          "two", "two", "one", "three"],
                    "C": np.random.randn(8),
                    "D": np.random.randn(8)})
df3
list(df3.groupby(["A", "B"]))
list(df3.groupby(["B", "A"]))

# =======================================

df.groupby("Property_Area").groups  # Should always return dict

# =======================================

list(df.groupby("Property_Area"))

# =======================================

df.groupby("Property_Area").size()

# =======================================

len(df.groupby("Property_Area"))  # number of dictionaries

# =======================================

df.groupby("Property_Area").indices

# =======================================

df.groupby("Property_Area").indices.keys()

# =======================================

df.groupby("Property_Area").indices.values()

# =======================================

# will return num of property area groups x num of gender groups (6)
df.groupby(["Property_Area", "Gender"]).groups

# =======================================

df.groupby(["Property_Area", "Gender"]).get_group(("Rural", "Male"))
# =======================================

for name, group in df.groupby(["Property_Area", "Gender"]):
    print(name)
    print(group)

# =======================================

# create a groupby var that groups key1 by key 2
df["Gender"].groupby(df["Property_Area"]).groups

# =======================================

# create a groupby var that groups the entire dataframe by key 2
df.groupby(df["Property_Area"]).groups

# =======================================

df4 = pd.DataFrame(
    {"X": ["B", "D", "A", "C", "A", "B"], "Y": [4, 5, 9, 2, 3, 7]})
df4.groupby("X").sum()  # will sort automatically
df4.groupby("X", sort=False).sum()

# =======================================

df.Property_Area == "Urban"

# =======================================

df[df.Property_Area == "Urban"]

# =======================================

g = df.groupby("Property_Area")
g.get_group("Urban")

# =======================================

list(g)[0]

# =======================================

list(g)[0][1]

# =======================================

g.sum()

# =======================================

g.mean()

# =======================================

g.describe()

# =======================================

x = "6"
x+"y"

# =======================================

x+10  # error cus string cannot be added to an int

# =======================================

pd.to_numeric(x) + 10  # Change string to number

# =======================================

g2 = df.groupby("Gender")
g2.groups

# =======================================

g2.LoanAmount.sum()

# =======================================

g3 = df.groupby(["Property_Area", "Gender"])
g3.aggregate(np.sum)

# =======================================

g.agg([np.sum, np.std, np.mean])
g.LoanAmount.agg([np.sum, np.std, np.mean])  # dont forget []
