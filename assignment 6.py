"""Write a menu-driven program to that calculates the (1) Sum (2) Difference (3) Product (4) Quotient (5)
Remainder (6) Larger out of two given numbers, based on the option selected by the user. Your program
should contain the following functions:
sum(num1, num2) – return the sum of num1 and num2
diff(num1, num2) – return the difference between num1 and num2
product(num1, num2) – return the product of num1 and num2
quotient(num1, num2) – return the quotient of num1 and num2
remainder(num1, num2) – returns the remainder of num1 and num2
menu() – prints the options
main() – calls the menu, reads two inputs and the option and calls the respective function based on the selected option."""
import math
def sum (num1 , num2):
    return (num1 + num2)
def diff (num1 , num2):
    return (num1 - num2 and num2 - num1)
def product (num1 , num2):
    return (num1 * num2 )
def quotient (num1 , num2):
    return(num1 // num2)
def remainder (num1 , num2):
    return (num1 % num2)
print("Choose the options")
print("1.sum")
print("2.diff")
print("3.product")
print("4.quotient")
print("5.remainder")
while True:
    choise = input("Enter the number (1/2/3/4/5): ")
    if choise in ('1','2','3','4','5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choise == '1':
            print("The sum of",num1 ,"+" ,num2 ,"=", sum(num1,num2))
        elif choise == '2':
            print("The difference between", num1 ,"-" ,num2 ,"=", diff(num1,num2))
        elif choise == '3':
            print("The produt of", num1, "*", num2, "=", product(num1, num2))
        elif choise == '4':
            print("The quotient of", num1 ,"//" ,num2 ,"=", quotient(num1,num2))
        elif choise == '5':
            print("The remainder of",num1 ,"%" ,num2 ,"=", remainder(num1,num2))
        break
    else:
        print("Invaild input")
