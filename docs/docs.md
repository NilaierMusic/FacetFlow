## Documentation for FacetFlow - a Python Library for Calculating Areas of Different Shapes  

### 1. Introduction

FacetFlow is a Python library used to calculate areas of various geometric shapes. The library provides a core functionality for triangle and circle shapes, including methods for calculating area and perimeter. However, it also allows users to extend this functionality by creating their own shape scripts. 

### 2. Installation

Before utilizing FacetFlow, ensure that Python interpreter is installed in your system. The library can be downloaded from our Github page at 'https://github.com/NilaierMusic/FacetFlow'. To install, navigate to the library's directory and run the `setup.py` script:

```
$ python setup.py install
```

### 3. How to Write a Custom Shape Calculation Script
To create a custom shape script, define a new class for the shape in question that inherits from the `Shape` abstract base class. 

For instance, to create a script computing for a rectangle, we would define a new class `Rectangle` in a standalone file `rectangle.py` like so:

```py
# rectangle.py

from .shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        
    def perimeter(self):
        return 2 * (self.length + self.width)
```

### 4. How to Use Existing Shape Calculation Script

```py
from shapes.circle import Circle
from shapes.triangle import Triangle

c = Circle(10) # radius
t = Triangle(3,4,5) # sides

print(c.area())
print(c.perimeter())

print(t.area())
print(t.perimeter())
```

### 5. How to Run Tests

The test_shapes.py suite contains comprehensive tests for all included shape classes. If you add your own shape classes, you should also add corresponding tests.

Here is an example of running the test suite using the provided AsciiTestRunner:

```
$ python test.py
```

### 6. Contributing

If you've created a new script for a geometric shape, we encourage you to contribute back to the project by making a pull request on our Github page.