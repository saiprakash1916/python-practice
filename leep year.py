num = int(input("Enter the year: "))
if (num % 4) == 0:
    if (num % 100) == 0:
        if (num % 400) == 0:
            print("{0} is a leep year".format(num))
        else:
            print("{0} is not leep year".format(num))
    else:
        print("{0} is a leep year".format(num))
else:
    print("{0} is not leep year".format(num))