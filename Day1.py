# Basic Python 
print("Hello World!")
print("Hi my name is Tanoy.", "I am 25 years old.")

name = "Tanoy" #string
age = 25       #int
price = 25.88  #float
old = True     #Boolean
ageue = None   #None

print("Hi, my name is", name ,"My name is ", age)
print(type(name), type(age), type(price), type(old), type(ageue))

a=2
b=4
sum = a+b
print(sum)

# Arithmetic Operators

a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #Reminder
print(a ** b) #Power Star (a^b)


# Relational Operators

a = 5
b = 2

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Assigment Operators

num = 10
num += 10 # num = num + 10
num **= 10 # num = num ^ 10

print("Num :", num)

# Logical Operators

a = 10
b = 5
print(not True)
print(not False)
print(not (a > b))

marks = True
age2 = True
age3 = False

print("AND Operators :", marks and age2)
print("AND Operators :", marks and age3)
print("AND Operators :", (a != b) or (a > b))

print("OR Operators :", marks or age3)
print("OR Operators :", (a == b) or (a > b))

# Type Convertion

a = 2
b = 4.5

sum = a + b
print(sum)

# Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Welcome", name)
print("Your age is: ", age)
print("Your marks is: ", marks)