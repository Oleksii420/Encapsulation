from FigureReader import FigureReader

if __name__ == '__main__':
    reader1 = FigureReader("input01.txt")
    reader2 = FigureReader("input02.txt")
    reader3 = FigureReader("input03.txt")
    figures1 = reader1.read()
    figures2 = reader2.read()
    figures3 = reader3.read()

    figures = figures1 + figures2 + figures3

    def max_per_area(figures):
        maxarea_result = ""
        maxperimeter_result = ""
        maxarea = -1
        maxperimeter = -1
        for figure in figures:
            area = figure.area()
            perimeter = figure.perimeter()
            if area > maxarea:
                maxarea = area
                maxarea_result = figure
            if perimeter > maxperimeter:
                maxperimeter = perimeter
                maxperimeter_result = figure
        return maxarea_result, maxperimeter_result

    area, perimeter = max_per_area(figures)


    print("Figure", area.__class__.__name__)
    print("area", area.area())
    print("Figure", perimeter.__class__.__name__)
    print("perimeter", perimeter.perimeter())
