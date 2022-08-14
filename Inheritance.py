"""

class <<Childclassname>>(baseblass):
    det __init__(self):
        baseclass().__init__(self)
"""
"""
class rectangle:
attributes - lenght & breadth
methods - perimeter, area

chil class = parallogram
- inhertts from rectange
- attributes = heights
- volume
"""


class Rectangl:
    def __self__(self, len=5, brd=6):
        self.length = len
        self.breadth = brd

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.breadth * self.length

    def show(self):
        print(f"Rectangl info:\n"
              f"Length: {self.length}\n"
              f"Breadth: {self.breadth}\n"
              f"Aread: {self.area()}\n"
              f"Perimeter: {self.perimeter()}")

class Parallelogram(Rectangl):
    def __init__(self, len, brd, height):
        super().__init__(self, len, brd)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

    def show(self):
        print(f"Rectangl info:\n"
              f"Length: {self.length}\n"
              f"Breadth: {self.breadth}\n"
              f"Area: {self.area()}\n"
              f"Perimeter: {self.perimeter()}"
              f"Volume: {self.volume()}")

    @classmethod
    def show(cls):
        cls.show()

