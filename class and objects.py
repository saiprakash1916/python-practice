class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("Config is: ",self.cpu,self.ram)
com1 = computer("processor is i7", "ram is 16gb ")
com2 = computer("processor is ryzen 5", "ram is 8gb")
com1.config()
com2.config()