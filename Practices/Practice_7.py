# =======================================
#  Intermediate Practice
# =======================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("https://bit.ly/2purmS1", sep=",")
df.head()

# =======================================

df.Gender == "Female"

# =======================================

df.loc[df.Gender == "Female"]

# =======================================

True or True
True or False
False or False
True and False
True and True
False and False

# =======================================

df[(df.Property_Area == "Urban") & (df.Gender == "Female")]  # NEED ()
# =======================================

# NEED ()     # | means OR
df[(df.Property_Area == "Urban") | (df.Gender == "Female")]

# =======================================

df[df.Gender.str.contains("Female")]  # Error cus the data contains NaN values

# =======================================

# no error cus the data does not contain NaN values
df[df.Property_Area.str.contains("Urban")]

# =======================================
# DETECTING NAN VALUES

df.info()
df.size
df.Self_Employed.value_counts()
df.Self_Employed.value_counts(dropna=False)

# =======================================

df["Gender"].value_counts(dropna=False)

# =======================================

df["Gender"].unique()

# =======================================

df["Gender"].nunique()
df["Gender"].nunique(dropna=False)

# =======================================

df[pd.isnull(df.LoanAmount)]

# =======================================
# INSERTING MISSING DATA

s = pd.Series([1, 2, 3])
s
s.loc[0] = None
s
s.loc[3] = None
s

# =======================================
# CALCULATIONS WITH MISSING DATA

pd.Series([np.nan]).sum()  # nan treated like 0
pd.Series([np.nan]).prod()  # nan treated like 1

# =======================================
# DROPPING AXIS LABELS WITH MISSING DATA

t = pd.DataFrame({"A": [np.nan, 2, 4, 6, 7],
                  "B": [4, np.nan, 6, 3, 8, ],
                  "C": [3, 6, 9, 12, 15]})
t
t.dropna(axis=0)
t.dropna(axis=1)
t["A"].dropna()

# =======================================
# ALLIGNMENT

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([1, 3, 5, 7, 8, 11])
s1+s2
s1.add(s2, fill_value=2)  # missing data replaced with fill value

# =======================================
# CONCATENATION

pd.concat([s1, s2], axis=0)
pd.concat([s1, s2], axis=1)

# =======================================
# SORTING

df.LoanAmount.sort_values()  # Sort the column in ascending

# =======================================

df.LoanAmount.sort_values(ascending=False)  # Sort the column in descinding

# =======================================

# Sort the whole dataframe in ascending according to 1 column
df.sort_values("LoanAmount")

# =======================================

# Sort the whole dataframe in descending according to 1 column
df.sort_values("LoanAmount", ascending=False)

# =======================================

df.sort_values(["LoanAmount", "ApplicantIncome"])
