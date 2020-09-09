# =======================================
#  Basics Practice
# =======================================

import random
import math
COST_MAIN = 38.00
COST_DRINK = 12.00
num_mains = int(input("Please enter number of mains:    "))
num_drinks = int(input("Please enter number of drinks:    "))
main_total = num_mains*COST_MAIN
drink_total = num_drinks*COST_DRINK
total_price = main_total+drink_total

print("{0} mains at ${1:.2f} is {2:.2f}".format(
    num_mains, COST_MAIN, main_total))
print("{0} mains at ${1:.2f} is {2:.2f}".format(
    num_drinks, COST_DRINK, drink_total))
print("please pay ${0:.2f}". format(total_price))

# =======================================

temp_celcius = float(input("Please enter your temperature in celcius:    "))
temp_farenheit = temp_celcius*1.8 + 32
print("{0:.2f} degrees celcius is {1:.2f} degrees farenheit".format(
    temp_celcius, temp_farenheit))

# =======================================


def air_fair(city):
    if city == "Auckland":
        return 200
    elif city == "Christchurch":
        return 280
    elif city == "Queenstown":
        return 300

# =======================================


print("Air Fair Cost: ", + air_fair("Auckland"))
print(air_fair("gewhjfb"))
.3

# =======================================


def renting_car(days):
    cost = days * 80
    if days > 7:
        cost = cost - 50
    elif days > 3:
        cost = cost - 20
    print("Renting Car Cost: ", + cost)
    return cost

# =======================================


renting_car(8)

# =======================================

print("Total Cost: ", + air_fair("Queenstown") + renting_car(5))

# =======================================

x = math.sqrt(25)
print(x)
dir(math)

# =======================================

help("math.log")
abc = math.log(10, 2)
print(abc)

# =======================================

math.pow(10, 2)

# =======================================

a = int(input("value of a:  "))
b = int(input("value of b:  "))
c = int(input("value of c:  "))
root_a = (-b + math.pow((math.pow(b, 2) - (4 * a * c)), 0.5)) / (2 * a)
root_b = (-b - math.pow((math.pow(b, 2) - (4 * a * c)), 0.5)) / (2 * a)
print("The roots are {0:.4} and {1:.4}".format(root_a, root_b))

# =======================================

angle = math.radians(16)

# =======================================

180*math.tan(angle)

# =======================================

random.randint(0, 100)

# =======================================

hyegywb = "blahblahblah"
hyegywb[4]

# =======================================

"PYTHON"[2]

# =======================================

name = "Fudge"
name[2:4]

# =======================================

maiza = 'maiza'
maiza[0:2]
maiza[:-2]
maiza[:-2]
maiza[::2]

# =======================================

vowel_string = "aeiou"
print(list(vowel_string))

# =======================================

print(list(range(10)))  # list num < 10
print(list(range(1, 5)))  # list 1 <= num < 5

# =======================================

text = "My name is Maiza"
mylist = text.split()
print(mylist)

# =======================================

nums = [3, 4, 1, 5, 10, 500]
for num in nums:
    print(num)

# =======================================

quote = "life is like a mirror"
words = quote.split()
print(words)
for m in words:
    print(m)

# =======================================

# repeating loop 10 times
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in num_list:
    print("Hello")

# =======================================

numbers = range(1, 101)
for sq in numbers:
    print(sq**2)

# =======================================

names = ["maiza", "rykiel", "melissa", "jin"]
names[1:3]  # index 1 to 2 (not including 3)
names[1:]  # index from 1 to end
names[:]  # the whole list

# =======================================

animal = ["dog", "cat", "kangaroo", "whale"]
print(animal)
animal.append("melissa")  # adding new element to END of list
print(animal)  # updated list
print(animal.index("dog"))
animal.insert(2, "rykiel")  # adding a new element to a specific index
print(animal)
for x in animal:
    print(x)
animal2 = ["eleplant", "panda", "hamster", "ant"]
animal.extend(animal2)  # adding everything from animal2 into animal
print(animal)
animal.reverse()
print(animal)
