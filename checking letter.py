# letter present or not
name = str(input("Enter the name: "))
chr = input("Enter the char: ")
if chr in name:
    print(chr,"in", name)
else:
    print("Not found in", name)