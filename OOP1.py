class Bottle:
    #attributes
    company='aqua'
    def __init__(self,c,h,r):
        self.color=c
        self.height=h
        self.radius=r
    def printVolume(self):
        print((22/7)*self.radius*self.radius*self.height)
    @classmethod
    def printCompany(cls,uName):
        print("The company name is "+cls.company+". Printed by "+uName)
    @staticmethod
    def sayHello():
        print("Hello")

b1=Bottle("Blue",35,3.5)
b2=Bottle("Black",50,3)

# print(b1.color)
# print(b2.color)

# b1.printVolume()
# b2.printVolume()

b1.printCompany("Leo")