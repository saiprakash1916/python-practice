class students:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("sai is good boy")
s1 = students(70,20,60)
s2 = students(80,85,75)
print(s1.avg())
print(students.getschool())
students.info()