from Triangle import Triangle
from Rectangle import Rectangle
from Trapezoid import Trapezoid
from Parallelogram import Parallelogram
from Circle import Circle

class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:

                data = line.split()

                type = data[0]
                try:
                    if type == "Triangle":
                        a, b, c = [float(el) for el in data[1:]]
                        triangle = Triangle(a, b, c)
                        figures.append(triangle)
                    elif type == "Rectangle":
                        a, b = [float(el) for el in data[1:]]
                        rectangle = Rectangle(a, b)
                        figures.append(rectangle)
                        pass
                    elif type == "Parallelogram":
                        a, b, h = [float(el) for el in data[1:]]
                        parallelogram = Parallelogram(a, b, h)
                        figures.append(parallelogram)
                        pass
                    elif type == "Circle":
                        r = float(data[1])
                        circle = Circle(r)
                        figures.append(circle)
                        pass
                    elif type == "Trapeze":
                        a, b, c, d = [float(el) for el in data[1:]]
                        trapezoid = Trapezoid(a, b, c, d)
                        figures.append(trapezoid)
                        pass
                except AssertionError:

                    pass

        return figures