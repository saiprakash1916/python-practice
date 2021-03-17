def divi(a,b):
    print(a/b)
def smart_divi(function):
    def inner (a,b):
        if a<b:
            a,b=b,a
        return function(a,b)
    return inner
divi = smart_divi(divi)
divi(2,4)