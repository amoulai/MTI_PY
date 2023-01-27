from math import sqrt


class ComplexIt(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexIt(self.real + other.real,
                         self.imag + other.imag)

    def __sub__(self, other):
        return ComplexIt(self.real - other.real,
                         self.imag - other.imag)

    def __mul__(self, other):
        return ComplexIt(self.real * other.real - self.imag * other.imag,
                         self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        sr, si, orl, oi = self.real, self.imag, other.real, other.imag  # short forms
        r = float(orl ** 2 + oi ** 2)
        return ComplexIt((sr * orl + si * oi) / r, (si * orl - sr * oi) / r)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def __neg__(self):  # defines -c (c is ComplexIt) return ComplexIt(-self.real, -self.imag)
        def __eq__(self, other):
            return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)

    def __repr__(self):
        return 'ComplexIt' + str(self)

    def __pow__(self, power):
        raise NotImplementedError('self**power is not yet impl. for ComplexIt')

    def _illegal(self, op):
        print('illegal operation "%s" for ComplexIt numbers' % op)

    def __gt__(self, other): self._illegal('>')

    def __ge__(self, other): self._illegal('>=')

    def __lt__(self, other): self._illegal('<')

    def __le__(self, other): self._illegal('<=')


if __name__ == '__main__':
    a = ComplexIt(1, 5)
    b = ComplexIt(3, 2)
    # usual operations
    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a <= b)
    # addition with integer
    x = a + 4.5
    y = a + ComplexIt(4.5, 0)
    print(x, y, x == y)
