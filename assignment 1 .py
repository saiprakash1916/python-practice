"""Write a program to calculate the bill of a DTP work as follows. Use if-else statement to determine if the user wants typing or copying done.
a. The rate of typing Rs. 3/Page
b. Printing of first copy Rs.5/page and later every copy Rs.3/Page.
Given the number of pages, print the total cost."""
pages = int(input("Enter the how many pages type: "))
if pages:
    typecost = 3*pages
    print("Typing cost is ", typecost, "rupes")
if pages:
    pages=pages-1;
    copycost = (3*pages)+5
    print("copy cost is", copycost, "rupess")
print("Total cost is",typecost + copycost, "rupess")