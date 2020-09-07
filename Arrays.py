# =======================================
#  Arrays Basics
# =======================================

import numpy as np
temp = np.loadtxt('temperature.txt')
print(temp)

# =======================================

print("\"temp\" is a ", type(temp))
print("The type of elements inside the array \"temp\" is ", temp.dtype)

# =======================================

len(temp)

# =======================================
#  Arrays Indexing
# =======================================

print("The 2nd number is ", temp[1])
print("The 27th number is ", temp[26])
print("The 156th number is ", temp[155])

# =======================================

print("The 5th last number is ", temp[-5])

# =======================================


def get_index(year=None, month=None):
    if year == None:
        year = int(input("Please enter the year (from 1980 to 2000): "))
    if month == None:
        month = int(input("Please enter the month (1st to 12th): "))
    index = 0
    for y in range(1981, 2001):
        index = index + 1
        if y == year:
            index_2 = index
    if year == 1980:
        index_2 = 0
    index_3 = (index_2*12) + month - 1
    return index_3


get_index()

# =======================================

Feb1980 = get_index(1980, 2)
May1995 = get_index(1995, 5)
Aug2000 = get_index(2000, 8)
print("The temperature in February 1980 was ", temp[Feb1980], ". ",
      "The temperature in May 1995 was ", temp[May1995], ". ",
      "The temperature in August 2000 was ", temp[Aug2000], ".")

# =======================================
#  Arrays Slicing
# =======================================

print("The last 3 elements are ", temp[:-4:-1])

# =======================================

temp100to120 = temp[99:121]
print(temp100to120[::2])

# =======================================

temp_1995 = temp[get_index(1995, 1):get_index(1996, 1)]
print(temp_1995)

# =======================================
#   Slicing & References
# =======================================

new_array = (temp[4:15])
print(new_array)

# =======================================

new_array[1] = -50.0
print(new_array)
print(temp[4:15])
# the original array is changed because they are both pointing to the same data, hence why it is changed

# =======================================

new_array2 = new_array.copy()
new_array2[2] = -60
print(new_array2)
print(new_array)

# =======================================

new_array[1] = 9.4
print(new_array)
print(temp[4:15])

# =======================================
#   Advanced Indexing (List and Boolean Indexing)
# =======================================

print((temp[6], temp[171], temp[222]))

# =======================================

bigger_than_18 = temp[temp > 18]
print(bigger_than_18)

# =======================================

for temps in bigger_than_18:
    idx = [x[0] for x in np.where(temp == temps)]
    print(idx)

# =======================================
#   Data Analysis Using Array Methods
# =======================================

avg = np.mean(temp)
print("The average temperature is {0:.2f} degrees Celsius.".format(avg))

# =======================================

max = np.amax(temp)
print("The hottest temperature is " + str(max))

# =======================================

print(sum(temp[:-51:-1]))

# =======================================

first20min = np.amin(temp[0:21])
cells100_140 = np.amin(temp[100:141])
cells215_250 = np.amin(temp[214:251])
min_in_sections = [first20min, cells100_140, cells215_250]
print(np.amin(min_in_sections))

# =======================================

largerthan9 = np.mean(temp[temp > 9])
smallerthan12 = np.mean(temp[temp < 12])
both = [largerthan9, smallerthan12]
print(np.mean(both))

# =======================================

avg1981 = np.mean(temp[get_index(1981, 1):get_index(1982, 1)])
avg1984 = np.mean(temp[get_index(1984, 1):get_index(1985, 1)])
avg1995 = np.mean(temp[get_index(1995, 1):get_index(1996, 1)])
print("The average of the years 1981, 1984 and 1995 are {0:.2f}, {1:.2f} and {2:.2f} respectively"
      .format(avg1981, avg1984, avg1995))

# =======================================

jantemp = [temp[range(0, 252, 12)]]
np.max(jantemp)

# =======================================

winter_ave = []
index_3 = [5, 6, 7]
for year in range(1980, 2001):
    ave_t = temp[index_3].mean()
    winter_ave.append(ave_t)
    index_3 = list(np.array(index_3) + 12)

winter = np.array(winter_ave)
print("Average Winter Temperature")
print(winter)
year_i = winter.argmin()
year = year_i + 1980
print(year)

# =======================================

temp_f = temp*32
print(temp_f)
