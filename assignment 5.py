"""Perfect number is a positive integer which is equal to the sum of its proper positive divisors. Write a program
which prints all perfect numbers in a given interval. For example: 6 is the first perfect number. Proper
divisors of 6 are 1, 2, 3. Sum of its proper divisors = 1 + 2 + 3 = 6. Hence 6 is a perfect number."""
number = int(input("Enter the number: "))
sum = 0
for i in range(1,number):
    if number % i ==0:
        sum = sum +i
if (sum ==number):
    print("%d is perfect number" %number)
else:
    print("%d is not perfect number" %number)