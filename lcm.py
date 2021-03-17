#Given two numbers find the least common multiple (LCM) of those numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if (num1 > num2):
    max = num1
else:
    max = num2
while (True):
    if (max % num1 == 0 and max % num2 == 0):
        print(max)
        break
    max =+ 1