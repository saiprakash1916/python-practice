class students:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):       # This is only for adding of the marks.
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = students(m1,m2)
        return s3
    def __gt__(self, other):     #This is used to which is best(gt means grather then).
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
s1 = students(50,60)
s2 = students(80,85)
s3 = s1 +s2
print(s3.m1)
print(s3.m2)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")