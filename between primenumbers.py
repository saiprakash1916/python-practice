a = int(input("Enter the lower number: "))
b = int(input("Enter the upper number: "))
print("prime numbers between", a ,"and", b ,"are: ")
for num in range (a,b+1):
    if num>1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
