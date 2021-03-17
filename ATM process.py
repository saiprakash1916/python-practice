# ATM process
print("Welcome to the Bank")
print("Please insert the card")
pin = int(input("Enter the pin: "))
if pin == 1916:
    print("1.Withdrawl")
    print("2.Transfer money")
    print("3.pin change")
    print("4.Balance enquiry")
    choise = int(input("Enter the number "))
    if choise == 1:
        print("1.Savings")
        print("2.Credit")
        option = int(input("Enter the option: "))
        if option == 1:
            cash = int(input("Enter the amount"))
            balance = 50000 - cash
            if balance <= 50000:
                print("Balance left", balance)
                print("Thanks for visit")
            else:
                print("Insufficent amount")
                print("Thanks for visit")
        elif option == 2:
            cash = int(input("Enter the amount: "))
            balance = 50000 - cash
            if balance <= 50000:
                print("Balance left", balance)
                print("Thanks for visit")
            else:
                print("Insufficent amount")
                print("Thanks for visit")
    elif choise == 2:
        name = input("Enter the name of the reciver: ")
        acc = int(input("Enter the account number: "))
        if acc == 123456789 and name == "sai prakash":
            cash = int(input("Enter the amount: "))
            print("Transtion completed")
            print("Thanks for visit")
        else:
            print("Invalid inputs")
            print("Thanks for visit")
    elif choise == 3:
        old = int(input("Enter the old password: "))
        new = int(input("Entre the new password: "))
        print("password changed succwssfully")
        print("Thanks for visit")
    elif choise == 4:
        print("Balance lest in your account")
        print("50000/-")
        print("Thanks for vist...")
else:
    print("password Error...")
    print("Please try again...")
