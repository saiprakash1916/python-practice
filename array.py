from array import*
array = array("i",[])
n = int(input("Enter the length of the array: "))
for i in range (n):
    x= int(input("Enter the number: "))
    array.append(x)
print(array)
# And we can also find index value of the array to continue to program
value = int(input("Enter the search number: "))
k = 0
for e in array:
    if e == value:
        print(k)
        break
    k=k+1
