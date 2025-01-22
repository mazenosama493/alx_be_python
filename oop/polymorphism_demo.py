class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.width = width
        self.lenght = lenght
    def area(self):
        return self.width * self.lenght
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius