"""Write a Python program in which the user enters either 'A', 'B', or 'C'. If 'A' is entered, the
program should display the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is
entered, it displays 'Coconut'."""
letter = input("Enter the letter: ")
if letter == 'a':
    print("Apple")
elif letter == 'b':
    print("Banana")
elif letter == 'c':
    print("Coconut")
else:
    print("Not define")