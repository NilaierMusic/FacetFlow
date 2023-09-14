# triangle.py
from .shape import Shape
import math

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides of a triangle must have positive length.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("These sides do not form a triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, (sides[0] ** 2 + sides[1] ** 2), abs_tol=1e-9)

    def perimeter(self):  # new method
        return self.a + self.b + self.c

    def __str__(self):
        return f'Triangle with sides {self.a}, {self.b}, {self.c}, area {self.area()} and ' \
               f'is_right_triangle: {"Yes" if self.is_right_triangle() else "No"}'