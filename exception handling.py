# try and error method
print("Resourse open")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
try:
    print(a/b)
    k = int(input("Enter the password: "))
except ZeroDivisionError as e:
    print("Hey, you cannot divide a number as zero",e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something went worng...")
finally:
    print("Resourse colsed")