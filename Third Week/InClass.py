#Object Oriengted Stuff!
class LightSwitch():
    def __int__(self):  #Initalizer - constructor in Python [self or this - are used to refer to itself]
        self.switchIsOn=False
    
    def turnOn(self):   #When defining a function that uses a contructer, use the term, 'self' to refer to the constructor
        self.switchIsOn=True

    def turnOff(self):
        self.switchIsOn=False

def main(): #Private variables do NOT exist in PYTHON!
    l0 = LightSwitch()
    l1 = LightSwitch()
    print(l0.switchIsOn)
    l1.turnOn()
    l0.turnOn()
    print(l0.switchIsOn)
    print(l1.switchIsOn)
    l0.turnOff()
    print(l0.switchIsOn)
    l1.turnOff()

class DimmerSwitch():
    def __int__(self):
        self.switchIsOn=False
        self.brightness=0
    
    def turnOn(self):
        self.switchIsOn=False
    
    def raiseLevel(self):
        if self.brightness>10:
            self.brightness=self.brightness+1

    def lowerLevel(self):
        if self.brightness>0:
            self.brightness=self.brightness-1

    def show(self):
        print('Switch is on', self.switchIsOn)
        print('brightness is:', self.brightness)


def main2():
    d0 =DimmerSwitch()
    d1=DimmerSwitch()
    d0.turnOn()
    d0.show
    for count in range(5):
        d0.raiseLevel()
    d0.show
    d1.show()

#main2()

class Account():
    def __int__(self, name, balance, password):
        self.name=name
        self.balance=float(balance)
        self.password=password

    def deposit(self, amountToDepo, password):
        if password != self.password:
            print('Sorry, incorrect Password')
            return None
    
        if amountToDepo<0:
            print('You cannot depo a NEGATIVE NUMBER FOOL')
            return None
        
    def withdraw(self, amountToWith, password):
        if password != self.password:
            print('wrong pass')
            return None
        if amountToWith > self.balance:
            print('Not enough money')
            return None
        


class Power(object):
    default_exponent=2

    def __init__(self,exponent=default_exponent):
        self.exponent=exponent

    def of(self,x):
        return x ** self.exponent
        

class RealPower(Power): #To use inheritence in Python, Put the name of the class your inheriting from in ()!
    def of(self,x):
        if isinstance(self.exponent, int) or x>=0:  #Checks to make sure the number is okay
            return x ** self.exponent
        raise ValueError(
            'Fration powers of NEGATIVE NUMBERS are IMAGINARY'
        )

def main3():
    n0 = RealPower(5)
    print(n0.of(3))


main3()