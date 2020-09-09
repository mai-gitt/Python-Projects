# =======================================
#  Intermediate Practice
# =======================================
# =======================================

import matplotlib as plt
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

w = np.loadtxt("Data\\waveform2.txt")

# =======================================

plt.plot(w)
plt.show()

# =======================================

type(w)

# =======================================

print(w.mean())
print(w.max())
print(w.min())

# =======================================

T = 200
w > 200

# =======================================

print(w[w > 200])
print(w[w < -T])

# =======================================

len(w[w < -T]) + len(w[w > T])

# =======================================

plt.plot(w)
plt.axhline(y=T, color="red", linestyle="-")
plt.axhline(y=-T, color="red", linestyle="-")
plt.show()

# =======================================

x = np.where(w > T)
y = w[w > T]
plt.plot(w)
plt.scatter(x, y, color="purple")

# =======================================

max_index_tuple = argrelextrema(w, np.greater)
xx = max_index_tuple[0]
yy = w[xx]
print(yy)

# =======================================

plt.plot(w)
plt.scatter(xx, yy)
plt.show()

# =======================================

a = np.array([3, 6, 2, 1])
a.shape

# =======================================

vowel = ("a", "e", "i", "o", "u")
print(type(vowel))
print(vowel[2])
print("---------------")
for v in vowel:
    print(v)
print("---------------")
print(vowel.count("a"))

# =======================================

seq = [(1, 2, 3), (4, 5, 6), (6, 7, 8)]
for a, b, c in seq:
    print(a, b, c)

# =======================================

T = (3, 4, 5, 6)
T[0]

# =======================================

T[0] = 122  # error cus tuple cannot be assigned

# =======================================

T+(1, 2, 3, 4)
print(T)
T[5]  # error cus havent reassigned (index out of range)

# =======================================

T = T+(1, 2, 3, 4)  # no error cus reassigned
print(T)
T[5]

# =======================================

a = 10
b = 2
print("a is ", a)
print("b is ", b)
print("---------")
a, b = b, a  # swapping values
print("a is ", a)
print("b is ", b)

# =======================================

phonebook = {"Sarah": "47492020", "Alex": "8383830", "Tim": "4289570"}
# d = {"key1": value1, "key2": value 2, "key3": value3}
print(phonebook["Sarah"])

# =======================================

info = {}
info["name"] = "Sandy"
info["occupation"] = "hacker"
info

# =======================================

info["occupation"] = "manager"  # changing the occupation
info

# =======================================

info.get("name")

# =======================================

print(info.get("hsdcysbe"))

# =======================================

menu = {}
menu["Chicken Alfredo"] = 14.50
print(menu["Chicken Alfredo"])

menu["Fish"] = 10.30
menu["Seafood"] = 20.50
menu["Pasta"] = 5.30

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

# =======================================

print(menu.pop("Seafood"))

# =======================================

menu

# =======================================

my_dict = {"address": "46L", "phone": "234", "ID": 8428}
print(list(my_dict.items()))
print(list(my_dict.keys()))
print(list(my_dict.values()))

# =======================================

hex_to_binary_table = {"2": "0010", "0": "0000",
                       "3": "0011", "4": "0100", "1": "0001"}
for digit in hex_to_binary_table:
    print(hex_to_binary_table[digit])

the_keys = list(hex_to_binary_table.keys())
the_keys.sort()
print(the_keys)
for k in the_keys:
    print(k, hex_to_binary_table[k])

# =======================================

map = {"a": 10, "c": 30, "f": 20, "b": 15}
for v in map.values():
    print(v)
for k, v in map.items():
    print(k, v)

# =======================================

product_list = {"bread": 2.5, "milk": 3.8, "butter": 5.9}
product_list["potato"] = 100
print(product_list)

# =======================================

product_list.pop("milk")
print(product_list)

# =======================================

umm = input("What do you want to buy?  ")

# =======================================

print("The original price of the product is ", product_list[umm])

# =======================================

product_list[umm] = product_list[umm] * 0.8
print("The price of the product after 20% discount is ", product_list[umm])

# =======================================

for k in product_list:
    print(k, product_list[k])

# =======================================

shopping = input("all products here, separated with, :")
shopping_list = shopping.split(",")
print(shopping_list)

# =======================================

cost = 0
for item in shopping_list:
    print(item, product_list[item])
    cost = cost + product_list[item]

# =======================================

data1 = [3, 5, 8, 3, 1]
data2 = [4, 7, 3, 8, 1]

# =======================================

plt.plot(data1, "r*--", label="A")
plt.plot(data1, "go--", label="B")
plt.legend()
