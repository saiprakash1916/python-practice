"""Write a program to calculate the bill for internet browsing. The conditions are given below.
a. 1 hour - 20 Rs.
b. 1/2 hour - 10 Rs.
c. Unlimited hours in a day - 90 Rs.
The user should enter the number of hours spent on browsing."""
hour = float(input("How many hours spent: "))
if (hour==1):
    payamount = 20
    print("Bill is",payamount)
elif (hour<1):
    payamount = 10
    print("Bill is",payamount)
elif(hour>1):
    fixedamount = 90
    print("Bill is ",fixedamount)