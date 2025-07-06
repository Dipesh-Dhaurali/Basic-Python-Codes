"""
sharadha(cont.. #9 (41:54))
"""
#When the same operator is allowed to have
# different meaning according to the context

#code note
# i => real part
# j => imaginary part
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self, other):
        return Complex(self.real+other.real , self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real-other.real , self.img - other.img)

    def __eq__(self, other):
        return self.real==other.real , self.img == other.img

    def showComplex(self):
        print(f"{self.real}i + {self.img}j")



a=Complex(4,6)
b=Complex(1,3)

add=a+b
sub=a-b
equal=a==b
print(equal)

add.showComplex()
sub.showComplex()

