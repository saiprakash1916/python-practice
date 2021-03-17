class A:
    def __init__(self):       # This is constructor
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A):
    def __init__(self):  # This is also constructor but only print B
        super().__init__()     #After adding the super method we cam print A and B
        print("in B init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
a1 = B()
a1.feature1()
a1.feature2()
a1.feature3()
a1.feature4()