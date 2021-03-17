class A:
    def show(self):
        print("in A show")
class B(A):     # in this class B use the parent class
    pass
a1 = B()
a1.show()
   # or
class A:
    def show(self):
        print("in A show")
class B(A):     # in this class B use the own class
    def show(self):
        print("in B show")
a1 = B()
a1.show()