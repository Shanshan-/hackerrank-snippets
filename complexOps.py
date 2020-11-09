import math
# https://www.varsitytutors.com/hotmath/hotmath_help/topics/operations-with-complex-numbers

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        # use FOIL, and combine like terms:
        #  (ac−bd)+(ad+bc)i
        realComp = (self.real * no.real) - (self.imaginary * no.imaginary)
        imgComp = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(realComp, imgComp)

    def __truediv__(self, no):
        # multiply numerator and denominator by the complex conjugate of denominator
        #  complex conjugate of (a+bi) = (a-bi)
        #  ((ac + bd) + (bc − ad)i) / (c^2 + d^2)
        realComp = (self.real * no.real) + (self.imaginary * no.imaginary)
        imgComp = (self.imaginary * no.real) - (self.real * no.imaginary)
        denom = no.real ** 2 + no.imaginary ** 2
        return Complex(realComp / denom, imgComp / denom)

    def mod(self):
        # |a+bi| = sqrt(a^2 + b^2)
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

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
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')