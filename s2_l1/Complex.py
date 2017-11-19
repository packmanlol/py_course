
import math


class Complex:

    def __init__(self, re=0.0, im=0.0):
        self.re = re
        self.im = im

    def __add__(self, a):
        temp = Complex()
        temp.re = self.re + a.re
        temp.im = self.im + a.im
        return temp

    def __sub__(self, a):
        temp = Complex()
        temp.re = self.re - a.re
        temp.im = self.im - a.im
        return temp

    def __mul__(self, a):
        temp = Complex()
        temp.re = self.re*a.re - self.im*a.im
        temp.im = self.re*a.im + self.im*a.re
        return temp

    def __truediv__(self, a):
        temp = Complex()
        temp.re = (self.re*a.re + self.im*a.im)/(a.re ** 2 + a.im ** 2)
        temp.im = (a.re*self.im - self.re*a.im)/(a.re ** 2 + a.im ** 2)
        return temp

    def conjug(self):
        temp = Complex()
        temp.re = self.re
        temp.im = -1 * self.im
        return temp

    def __abs__(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def fi(self):
        return math.atan(self.im/self.re)

    def __pow__(self, power, modulo=None):
        temp = Complex()
        temp.re = abs(self) ** power * math.cos(power * self.fi())
        temp.im = abs(self) ** power * math.sin(power * self.fi())
        return temp

    def root(self, power):
        lst = []
        temp = Complex()
        for i in range(power):
            temp.re = abs(self) ** (1 / power) * math.cos((self.fi() + 2 * math.pi * i) / power)
            temp.im = abs(self) ** (1 / power) * math.sin((self.fi() + 2 * math.pi * i) / power)
            lst.append(temp)
        return lst

    def __str__(self):
        if self.im >= 0:
            return "{}+{} i".format(self.re, self.im)
        else:
            return "{}{} i".format(self.re, self.im)

