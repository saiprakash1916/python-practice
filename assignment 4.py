"""Write a Python program in which a student enters the number of college credits earned. If
the number of credits is greater than 90, 'Senior Status' is displayed; if greater than 60,
'Junior Status' is displayed; if greater than 30, 'Sophomore Status' is displayed; else,
'Freshman Status' is displayed."""
credits = int(input("Enter the credits: "))
if (credits>=90):
    print("Senior status")
elif (credits>=60):
    print("Junior status")
elif (credits>=30):
    print("Sophomore status")
else:
    print("Freshman status")