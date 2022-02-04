import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        l=(self.real+no.real)
        m=(self.imaginary+no.imaginary)
        return Complex(l,m).__str__()
        
    def __sub__(self, no):
        l=(self.real-no.real)
        m=(self.imaginary-no.imaginary)
        return Complex(l,m).__str__()
        
    def __mul__(self, no):
        l=(self.real*no.real-self.imaginary*no.imaginary)
        m=(self.real*no.imaginary+self.imaginary*no.real)
        return Complex(l,m).__str__()

    def __truediv__(self, no):
        base=(no.real**2+no.imaginary**2)
        l=(self.real*no.real+self.imaginary*no.imaginary)/base
        m=(self.imaginary*no.real-self.real*no.imaginary)/base
        return Complex(l,m).__str__()

    def mod(self):
        z=(self.real**2+self.imaginary**2)**(1/2)
        return ("%.2f+0.00i" % z).__str__()

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
