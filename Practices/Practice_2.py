# =======================================
#  Intermediate Practice
# =======================================

import matplotlib.pyplot as plt
import numpy as np  # if never *import numpy as np*,
# everytime use np function, must write in the form of (eg.)numpy.array
a = [4, 5, 6, 7, 9, 2, 3]
y = np.array(a)
high = y > 5
y[high]
print(high)

# =======================================

nums = np.array([10, 4, 20, 6, 7, 9])
big_nums = nums[nums > 8]
good_nums = nums[((nums > 2) & (nums < 10))]
print(big_nums)
print(good_nums)
nums[[2, 3, 5]]

# =======================================

a = np.array([2, 5, 7, 3, 9])
np.sqrt(a)
print(a)
a = np.sqrt(a)
print(a)

# =======================================

height_list = [191, 184, 185, 180, 152, 190, 195, 180, 195, 190]
heights = np.array(height_list)
print(heights)

# =======================================

type(heights)

# =======================================

weights = np.array([220, 210, 225, 180, 230, 235,
                    210, 205, 170, 190])  # in pounds
weightsKG = weights * 0.453592  # in kg
heightsM = heights / 100
BMI = weightsKG/(heightsM**2)
print(BMI)

# =======================================

np.median(heightsM)

# =======================================

np.random.randint(30, 50, size=20)

# =======================================

a = np.array([4, 7, 1, 8])
b = a[1:3]
b

# =======================================

b[0] = 1000
b

# =======================================

a

# =======================================

c = a  # changing c changes a
c[3] = -555
c

# =======================================

a

# =======================================

d = a.copy()  # changing d does not change a
d

# =======================================

d[3] = 3030303
d

# =======================================

a

# =======================================

e = a[[1, 3]]  # e does not change a
e

# =======================================

f = a[a > 2]  # f does not change a
f

# =======================================

a

# =======================================

plt.plot([30, 70, 20, 50, 40, 60, 30])
plt.show()

# =======================================

plt.plot(['0', '5', '10', '15', '20'], [0, 100, 80,
                                        800, 1000], color='black', linestyle='--')
plt.xlabel("your age")
plt.ylabel("retardedness")
plt.show()

# =======================================

plt.hist(a, bins=5)
