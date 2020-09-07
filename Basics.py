# =======================================
#   Baby Stuff
# =======================================
import random
your_name = (input("What is your name?  "))
print("Hello " + your_name)
your_interviewer = (input("What is interviewer's name?  "))
your_time = (input("What time is your appointment?  "))
print(your_name + " will have an appointment with " +
      your_interviewer + " at " + your_time)

# =======================================

print("\nTRIANGLE AREA\n")
base = float(input("What is the base length of your triangle?  "))
height = float(input("What is the height of your triangle?  "))
area = base*height*0.5
print("The area of the triangle is {0:.2f}cm\u00b2".format(area))


# =======================================
#   Definining and Calling a Function
# =======================================

print("\nRANGE 1\n")


def number(num):
    blah = float(num)
    if num > 100:
        print("{0} is outside given range".format(blah))
    elif num < 0:
        print("{0} is outside given range".format(blah))
    else:
        print("{0} is in the range".format(blah))


number(110)
number(1.5)
number(-5)

# =======================================

print("\nRANGE 2\n")
min_num = float(input("Please enter lowest num:    "))
max_num = float(input("Please enter highest num:    "))


def number(num):
    blah = float(num)
    if num > max_num:
        print("{0} is outside given range".format(blah))
    elif num < min_num:
        print("{0} is outside given range".format(blah))
    else:
        print("{0} is in the range".format(blah))


number(110)
number(1.5)
number(-5)

# =======================================

print("\nINITIALS\n")


def get_initials(first_name="", last_name=""):
    return print(first_name[0] + last_name[0])


get_initials('Maiza', 'Rehan')
get_initials('Your', 'Name')
get_initials('Michael', 'Jackson')

# =======================================
#   If Statements
# =======================================

print("\n")
num = random. randint(1, 9)
var = input("Guess my number:  ")
if var.isnumeric():
    if num > int(var):
        print("Too Low")
    elif num < int(var):
        print("Too High")
    else:
        print("Exactly Right!!")
else:
    print("It is not a number")

# =======================================

print("\nEVEN OR ODD\n")
num = int(input("What is your number?  "))
if num % 2 == 0:
    print("Your number is an even number.")
else:
    print("Your number is an odd number.")

# =======================================

print("\nPOINTS NEEDED FOR GRADUATION\n")
student_points = int(input("How many points do you have?  "))
if student_points == 360:
    print("Congratulations, you have enough points for graduation!")
elif student_points > 360:
    print("Congratulations, you have enough points for graduation!")
elif student_points < 360:
    points_needed = 360 - student_points
    print("You still need {0} point(s) for graduation".format(points_needed))

# =======================================

print("\nCOIN TOSS\n")
coin_toss = random.randrange(1, 3)
if coin_toss == 1:
    print("Heads")
else:
    print("Tails")

# =======================================

print("\nWEEKLY PAY\n")
hours = float(input("Hours worked per week:  "))
if hours > 50:
    print("Warning! Your should rest!")
rate = float(input("Hourly Pay:  "))
if hours < 40:
    weekly_pay = hours * rate
else:
    weekly_pay = (((hours - 40) * 2 * rate) + (40 * rate))
print("Your weekly pay is ${0:.2f}".format(weekly_pay))

# =======================================
#   For Loops
# =======================================

print("\nSUM\n")
range(1, 101)
print(sum(range(1, 101)))

# =======================================

print("\IFZZBUZZ GAME\n")
numbers = range(1, 31)
for x in numbers:
    output = ""
    if x % 3 == 0:
        output += "Fizz"
    if x % 5 == 0:
        output += "Buzz"

    if output == "":
        output = x
    print(output)

# =======================================
#   Strings
# =======================================

print("\nCOUNT UPPER & LOWER\n")
words = input("Enter your words: ")
lower_case = 0
upper_case = 0
for letter in words:
    if(letter.islower()):
        lower_case += 1
    elif(letter.isupper()):
        upper_case += 1
print("Number of lower case characters : {0}.".format(lower_case))
print("Number of upper case characters : {0}.".format(upper_case))

# =======================================

print("\nIS IT A PALINDROME?\n")
my_palindrome = (input("Enter text:  "))
checking = my_palindrome.replace(" ", "")
if checking == ''.join(reversed(checking)):
    print("{0} is a palindrome!".format(my_palindrome))
else:
    print("{0} is not a palindrome.".format(my_palindrome))

# =======================================
#   Lists
# =======================================

print("\nCOLOUR LIST\n")
colour_list = ["Green", "Black", "Red", "White"]
print(colour_list[0] + ", " + colour_list[3])

# =======================================

print("\nGRADE CALC\n")
assignment_scores = input("Input your scores split by commas: ")
if assignment_scores.count(',') > 5:
    print("WARNING! Input cannot be split into 6 numbers.")
    assignment_scores = input("Input your scores split by commas : ")
assignment_list = assignment_scores.split(",")
ass_1 = (int(assignment_list[0])/100 * 10)
ass_2 = (int(assignment_list[1])/100 * 10)
ass_3 = (int(assignment_list[2])/100 * 10)
ass_4 = (int(assignment_list[3])/100 * 15)
ass_5 = (int(assignment_list[4])/100 * 20)
exam_1 = (int(assignment_list[5])/100 * 35)
print("Your total score for the course is ", +
      ass_1 + ass_2 + ass_3 + ass_4 + ass_5 + exam_1)

# =======================================

print("\nFREQUENCY OF ELEMENTS\n")
element_input = input("Write your elements split by commas: ")
element_list = element_input.split(",")
var = {}
for item in element_list:
    if item in var:
        var[item] = var.get(item)+1
    else:
        var[item] = 1

for hi, hello in var.items():
    print(str(hi)+':'+str(hello))
