class students:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self, a = None, b = None, c = None):    # method over loading in this none menas zero.
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s
s1 = students(80,85)
print(s1.sum(10,30))