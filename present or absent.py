# Names present or absent program
names = ["sai","prakash","chinni","dharani","ddd"]
name = str(input("Enter the name: "))
aa=False     # if name is not given next step direct to else statement
for i in names:
     if i == name:
        aa = True
        break
if(aa):
    print(name, "present")
else:
    print(name, "not present")