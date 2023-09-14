# circle.py
from .shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):  # new method
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle with radius {self.radius} and area {self.area()}'