#Write a program that takes age as input and prints whether the person is eligible for voting or not.
age = int(input("Enter the age: "))
if age >= 18:
    status = "Eligible"
else:
    status = "Not Eligible"
print("You are", status, "for vote.")