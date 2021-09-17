class RealNumber:
    def __init__(self, number=0):
        self.number = number
        
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    
    def __str__(self):
        return str(self.number)
    
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        r = self.real + int(other.real)
        i = self.img + int(other.img)
        # return ComplexNumber((self.real + other.real), (self.img + other.img))
        return f"{r} + {i}i"
    def __sub__(self, other):
        r = self.real - int(other.real)
        i = self.img - int(other.img)

        # return ComplexNumber((self.real + other.real), (self.img + other.img))
        return f"{r} - {abs(i)}i"
    def __str__(self):
        r = self.real
        i = self.img
        return f"{r} + {i}i"




r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1.number, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)