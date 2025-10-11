class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Square(Polygon, Rectangle):
    pass
