import math

num1 = input("Please enter the first number ")
num1 = float(num1)
num2 = input("Please enter the second number ")
num2 = float(num2)


num3 = int(math.ceil(num1/num2))
print("The result of the division is: " + str(num3))