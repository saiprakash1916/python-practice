a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print ("Even numbers between", a,"and", b ,"are: ")
for num in range (a,b+1):
    if (num % 2)==0:
        print("{0}".format(num))