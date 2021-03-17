number = int(input("Enter the number: "))
count = 0
while (number > 0):
    number = number // 10
    count +=1
print("Number of digits in a given number is: %d " %count)
