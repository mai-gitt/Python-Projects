# =======================================
#  Intermediate Practice
# =======================================

from Bio import SeqIO
import Bio
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("https://bit.ly/2hjHvag")
df.head()
df.shape

# =======================================
# KNN
# PREPROCESSING 1

df.columns = ["id_number", "Clump_Thickness", "Uniformity_of_Cell_Size",
              "Uniformity_of_Cell_Shape", "Marginal_Adhesion", "Single_Epithelial_Cell_Size",
              "Bare_Nuclei", "Bland_Chromatin", "Normal_Nucleoli", "Mitoses", "Class"]
df.head()

# =======================================
# PREPROCESSING 2

df.replace("?", 0, inplace=True)  # replace all ?s with 0

# =======================================

KNN = KNeighborsClassifier(n_neighbors=3)
KNN

# =======================================
# FITTING THE MODEL WITH THE DATA

feature = df.drop(["Class", "id_number"], axis=1)
feature.head()
label = df.Class

X_tr, X_te, y_tr, y_te = train_test_split(feature, label, test_size=0.4)
# X_tr means training input
# y_tr means training output
# X_te means test input
# y_te means test output
X_tr.shape
X_te.shape
y_tr.shape
y_te.shape

KNN.fit(X_tr, y_tr)
# feature.head()

# =======================================
# MAKING OBSERVATIONS BASED ON NEW OBSERVATIONS

y_pr = KNN.predict(X_te)
y_pr

# =======================================
# EVALUATION

# number of correctly classified samples/ total num of samples
metrics.accuracy_score(y_te, y_pr)

# =======================================
# DIFFERENT CLASSIFICATION ALGORITHM

# Step 1. Import the class
# from sklearn.linear_model import LogisticRegression

# Step 2. Intantiate the model
lr = LogisticRegression()

# Step 3. Fit the model with data
lr.fit(X_tr, y_tr)

# Step 4. Prediction
y_prlr = lr.predict(X_te)

# Step 5. Evaluation
metrics.accuracy_score(y_te, y_prlr)

# =======================================
# LINEAR REGRESSION

#from sklearn.datasets import load_boston
bdf = load_boston()
print(bdf)
bdf.data
bdf.feature_names
bdf.target

# =======================================

# Step 1. Import the class
#from sklearn.linear_model import LinearRegression

# Step 2. Instantiate the estimator
LR = LinearRegression()

##### PREPROCESSING #####
X = pd.DataFrame(bdf.data, columns=bdf.feature_names)
X.head()
y = pd.DataFrame(bdf.target)
y.head()

# =======================================

# Step 3. Fit the model with the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y)  # test_size = 0.4 (can customise 0-1)
LR.fit(X_train, y_train)

# =======================================

LR.intercept_
LR.coef_

# =======================================

# Step 4. Make predictions
y_pred = LR.predict(X_test)
plt.scatter(y_test, y_pred)  # expect to see linear behaviour

# =======================================

# Evaluations
# MAE #the bigger the less accurate
metrics.mean_absolute_error(y_test, y_pred)
metrics.mean_squared_error(y_test, y_pred)  # MSE

# =======================================
# BIOPYTHON

# import Bio
# from Bio import SeqIO
list1 = list(SeqIO.parse("Data\\ls_orchid.fasta", "fasta"))

# =======================================

for k in list1:
    print(k)

# =======================================

list1[0]

# =======================================

s_red = list1[-1]

# =======================================

s_red.descrription

# =======================================

s_red.seq

# =======================================

seq1 = s_red.seq

# =======================================

print(type(seq1))

# =======================================

print(seq1)

# =======================================

seq1.count("GA")
