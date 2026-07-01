from inheritance import Calc,AdvCalc
    

# 4 attr, 1 meth 

# print(Bottle.color)
# Bottle.printVolume()

# Bottle.printCompany()

# b1=Bottle()
# b2=Bottle()
# b3=Bottle()

# b1.color="Black"

# print(b1.color)
# print(b2.color)
# print(b3.color)

# print(b2.color)

# b1.sayHello()

# b2.sayHello() # Bottle.sayHello(Bottle)

# a=10 #int
# b="Hello" 
# c=[1,2,3]

# print(type(b1)) #<class '__main__.Bottle'>

class SciCalc(AdvCalc, Calc):
    def __init__(self):
        self.version="1.0.0.0"
    def printVersion(self):
        print(self.version)
    @staticmethod
    def mod(a,b):
        print(a%b)

c1=SciCalc()
# c1.add(9,10)

# c1.printVersion() #SciCalc.printVersion(c1)
c1.mod(10,9)