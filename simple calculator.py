def add (x , y):
    return x + y
def subtract (x , y):
    return x - y
def multiply (x , y):
    return x * y
def divide (x , y):
    return x / y
def module (x , y):
    return x % y
print("Choose one the above")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.module")
while True:
    choise = input("Enter choise (1/2/3/4/5) : ")
    if choise in ('1', '2', '3','4','5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choise == '1':
            print (num1, "+", num2,"=", add(num1,num2))
        elif choise == '2':
            print (num1, "-", num2,"=", subtract(num1,num2))
        elif choise == '3':
            print (num1, "*", num2,"=", multiply(num1,num2))
        elif choise == '4':
            print (num1, "/", num2,"=", divide(num1,num2))
        elif choise == '5':
            print (num1, "%", num2,"=", module(num1,num2))
        break
    else:
        print("Invalid input")