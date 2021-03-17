Telugu = float(input("Enter the telugu marks: "))
English = float(input("Enter the english marks: "))
Hindi = float(input("Enter the hindi marks: "))
Maths = float(input("Enter the maths marks: "))
Science = float(input("Enter the science marks: "))
Social = float(input("Enter the social marks: "))
total = Telugu + English + Hindi + Maths + Science + Social
percentage = (total / 600) * 100
print("Toatal marks = %2f" % total)
print("Marks percentage = %2f" % percentage)
if (percentage >= 101):
    print ("Dis qualifie")
elif (percentage >= 90):
    print("A Grade")
elif (percentage >= 80):
    print("B Grade")
elif (percentage >= 70):
    print("C Grade")
elif (percentage >= 60):
    print("D Grade")
elif (percentage >= 50):
    print("E Grade")
else:
    print("Fail")