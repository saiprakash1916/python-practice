class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
class B:
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
class C(A,B):
    def feature5(self):
        print("Feature 5 is working")
    def feature6(self):
        print("Feature 6 is working")
a1 = A()
b1 = B()
c1 = C()
a1.feature1()
a1.feature2()
b1.feature3()
b1.feature4()
c1.feature5()
c1.feature6()