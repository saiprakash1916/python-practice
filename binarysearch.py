pos = -1
def search (list,n):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list [mid] == n:
            globals()["pos"] = mid
            return True
        else:
            if list [mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    return False
list = [10, 20, 30, 40, 50]
n = 40
if search(list,n):
    print("Found", pos+1)
else:
    print("Not found")