import math
class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        result = 0
        if self.b != self.a:
            height = abs(self.a ** 2 - ((self.b - self.a) ** 2 + self.a ** 2 - self.b ** 2) / (2 * (self.b - self.a)))

            result = 0.5 * height * (self.a + self.b)
        return result



