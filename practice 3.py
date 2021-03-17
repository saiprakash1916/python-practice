class students:     #Outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()
    def show(self):    #This print about student class
        print(self.name, self.rollno)
        self.lap.show()
    class laptop:       #Inner calss
        def __init__(self):
            self.brand = "Dell"
            self.cpu = "i7 processor"
            self.ram = "16 GB Ram"
            self.stroage = "1TB HDD and 256 GB SSD"
        def show(self):     #This print about laptop class
            print(self.brand, self.cpu, self.ram)
s1 = students("sai", 10)
s1.show()
lap1 = students.laptop()
