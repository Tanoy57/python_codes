# Write a program to input 2 number & print there sum

a,b = int(input("Enter num1: ")),int(input("Enter num2: "))
sum = a + b

print("The sum is:",sum)
print("The sub is:",a-b)

# Write a program to input side of a square & print its area

size = float(input("Enter the size: "))
area = size ** 2   # We also write in next line , area **= 2

print("The area is: ",area)

# Write a program 2 floating point numbers & print their average 

a,b = float(input("Num1: ")), float(input("Num2: "))
average = (a + b) / 2

print("The average are: ", average)

# Write a program to input 2 int number , a and b. Print true if a is greater than or equal to b. If not than print false

a,b = int(input("Enter num1: ")),int(input("Enter num2: "))
print("Input statement are : ", a >= b)

