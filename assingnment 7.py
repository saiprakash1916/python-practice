#program to find the length of the string "refrigerator" without
#using len function
word = str(input("Enter the word: "))
counter = 0
for i in word:
    counter = counter + 1
print("length of the word is", counter)