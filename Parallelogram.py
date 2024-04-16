class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def area(self):
        area = self.a * self.h
        return area