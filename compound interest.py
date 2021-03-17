import math
principal_amount = float(input("Enter the principal amount: "))
rate_of_interset = float(input("Enter the tare of interest: "))
time_period = float(input("Enter the time period in years: "))
ci_future = principal_amount * (math.pow((1 + rate_of_interset / 100), time_period))
compound_interest = ci_future - principal_amount
print("compound interest for principal amount {0} = {1}".format(principal_amount, compound_interest))
print("Feture compound interest for princiapl amount {0} = {1}".format(principal_amount, ci_future))
