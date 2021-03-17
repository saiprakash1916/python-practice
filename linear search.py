pos = -1
def search (list,n):
    i = 0
    while i < len(list):
        if list [i] == n:
            globals() ["pos"] = i
            return True
        i = i + 1
    return False
list = [5, 10, 13, 19, 25]
n = 13
if search(list,n):
    print("Found", pos+1)
else:
    print("Not found")