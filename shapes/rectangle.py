# rectangle.py 
from .shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):  
        return 2 * (self.length + self.width)
        
    def is_square(self):
        return self.length == self.width

    def __str__(self):
        return f'Rectangle with length {self.length}, width {self.width}, area {self.area()}, ' \
               f'perimeter {self.perimeter()} and is_square: {"Yes" if self.is_square() else "No"}'