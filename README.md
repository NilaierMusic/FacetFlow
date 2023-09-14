![FacetFlow Logo](/docs/title.png 'FacetFlow Logo')
# FacetFlow

FacetFlow is a comprehensive Python library for calculating areas of various geometric shapes with incredible ease. The library comes with core calculations for common shapes like triangle and circle, but is designed with extensibility in mind — allowing you to whip up your own scripts for additional shapes as needed.

## Contents

1. [Description](#Description)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Tests](#Tests)
5. [Contribute](#Contribute)

### Description

FacetFlow provides a set of tools for performing area calculations on different geometric shapes. It's an ideal library for tasks which require a high level of precision and a wide range of shape options. The library includes built-in classes for common shapes, and can easily be extended to include additional shapes. These scripts can be contributed back to the project to broaden our shape library further, or kept for specific use cases — the choice is yours.

### Installation

To start using FacetFlow:

1. Ensure Python is installed on your system
2. Download the library from our Github repository.
3. Navigate to the library directory and run the `setup.py` script:

```
$ python setup.py install
```

### Usage

Import the shape classes from the module and create instances of the shapes you wish to calculate.

E.g., to calculate the area of a circle and a triangle:

```python
from shapes.circle import Circle
from shapes.triangle import Triangle

c = Circle(10) # radius
t = Triangle(3,4,5) # sides

print(c.area())
print(c.perimeter())

print(t.area())
print(t.perimeter())
```

### Tests

A comprehensive test suite is included with FacetFlow. To run the tests, use the provided AsciiTestRunner:

```
$ python test.py
```

### Contribute

Contributions to extend the shape library in FacetFlow are welcomed. If you've created a script for a geometric shape, consider making a pull request on our Github page so others in the community can utilize it.
</details>