num = int(input("Enter the number: "))
factorial = int(input("Enter the factorial: "))
if num <0 :
    print("sorry, factorial does not exit negative numbers")
else:
    for i in range (1,num+1):
        factorial = factorial+1
    print("The facorial of", num,"is",factorial)
