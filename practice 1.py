class car:
    wheel = 4
    def __init__(self):
        self.mil = 10
        self.brand = "BMW"
c1 = car()
c2 = car()
c1.mil = 8
car.wheel = 5
print("Brand is" , c1.brand, " and Maillage is", c1.mil, " and Number of wheels is", c1.wheel)
print("Brand is", c2.brand, "and Maillage is",c2.mil,  "and Number of wheels is",c2.wheel)