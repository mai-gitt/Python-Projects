# =======================================
#  Intermediate Practice
# =======================================
# =======================================

import matplotlib as plt
import pandas as pd
import numpy as numpy

# =======================================

# if tsv file --> pd.read_csv("nameoffile.tsv", sep = "\t")
farm = pd.read_csv("Data\\maorifarm.csv")
print(farm)

# =======================================

farm.dtypes

# =======================================

birds = pd.read_csv("Data\\Birds.csv")
birds

# =======================================

birds.dtypes  # object means string

# =======================================

farm.index

# =======================================

farm.columns

# =======================================

farm.values
# =======================================

farm.size  # no of cells

# =======================================

farm.shape  # rows, columns

# =======================================

print(farm.shape[0])  # just no of rows
print(farm.shape[1])  # just no of columns

# =======================================

farm > 200

# =======================================

farm["Kiwifruit"]*2.47  # changing from square km to acres

# =======================================

farm.info()

# =======================================

dir(farm)

# =======================================

farm["Onions"]

# =======================================

d = pd.DataFrame({"a": [1, 2], "b": [3, 4]}, index=["one", "two"])
d

# =======================================

d.loc["two"]  # row two

# =======================================

farm.iloc[2]  # 2nd row

# =======================================

farm.at[2, "Kiwifruit"]  # 1 row and 1 column only --> 1 cell
# specify the index of row and name of column

# =======================================

farm.iloc[0:3]

# =======================================

farm.iat[2, 1]  # specify the number of rhe row and number of column

# =======================================

farm[["Avocados", "Wine_grapes"]]

# =======================================

farm[2:4]

# =======================================

farm.loc[2:4, ["Kiwifruit"]]

# =======================================

# the first part is start from 1 and exclusive of the end
farm.iloc[2:5, [0, 1]]
# the second part is start from 0 inclisive of the end

# =======================================

farm.loc[5] = [2015, 300, 70, 400, 300, 200]
farm

# =======================================

farm["Orange"] = [20, 30, 40, 50, 60, 10]
farm

# =======================================

farm.at[3, "Orange"] = 700
farm

# =======================================

farm.drop("Orange", 1)  # must specify axis --> 0 is row 1 is column

# =======================================

farm.drop([2, 3], 0)  # doesnt change original data
# changing anything must be an assignment --> farm = farm.drop([2,3], 0)

# =======================================

farm

# =======================================

farm["Kiwifruit"] < 315

# =======================================

farm[farm["Kiwifruit"] < 315]

# =======================================

farm[farm["Onions"] == 212.0]

# =======================================

farm.plot()

# =======================================

farm.plot(x="Year")

# =======================================

farm.plot(x="Year", kind="bar")

# =======================================

farm.plot(kind="kde", x="Year")

# =======================================

farm.mean()

# =======================================

frame = pd.DataFrame(data)
frame

# =======================================

farm.sum()

# =======================================

farm

# =======================================

farm = farm.drop("Orange", 1)
farm

# =======================================

farm.sum()

# =======================================

fn = farm.iloc[::, [1, 2, 3, 4, 5]]
fn.sum()

# =======================================

fn["Total"] = fn.sum(axis=1)  # does not change farm
fn

# =======================================

fn.max(axis=1)

# =======================================

# salaries = pd.read_csv(
#     "http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
salaries = pd.read_csv("Data//Salaries")
salaries

# =======================================

salaries.head(10)  # first 10 rows

# =======================================

salaries.tail(10)  # last 10 rows

# =======================================

salaries.columns  # list column names

# =======================================

salaries.axes  # list row lables and column names

# =======================================

salaries.ndim  # number of dimensions

# =======================================

salaries.size  # number of elements

# =======================================

salaries.shape  # return a TUPLE representing the dimentionality

# =======================================

salaries.values  # NUMPY representation of the data

# =======================================

salaries.dtypes  # list the types of columns
