import unittest
import pkgutil
import inspect
from shapes.shape import Shape

class ShapeTests(unittest.TestCase):
    shapes = []
    results = {} # Add this line

    @classmethod
    def setUpClass(cls):
        package = "shapes"
        prefix = f"{package}."
        for importer, modname, ispkg in pkgutil.iter_modules():
            if not ispkg and modname.startswith(prefix):
                module = __import__(modname, fromlist="dummy")
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, Shape) and obj is not Shape:
                        cls.shapes.append(obj)

    def test_areas(self):
        """Compute areas for all shape classes."""
        for shape in self.shapes:
            instance = shape(2)
            self.assertAlmostEqual(instance.area(), instance.expected_area)

    def test_perimeters(self):
        """Compute perimeters for all shape classes."""
        for shape in self.shapes:
            instance = shape(2)
            self.assertAlmostEqual(instance.perimeter(), instance.expected_perimeter)
            
    def test_invalid_triangle(self):
        """Triangle should throw an error if sides can't form a triangle"""
        from shapes.triangle import Triangle
        with self.assertRaises(ValueError):
            Triangle(3,4,10)
            
    def test_negative_radius_circle(self):
        """Circle should throw an error if the radius is negative"""
        from shapes.circle import Circle
        with self.assertRaises(ValueError):
            Circle(-2)
            
    def test_circle_area_calculation(self):
        """Verify area calculation for Circle."""
        from shapes.circle import Circle
        import math

        for r in range(1, 10):  # testing multiple values
            circle = Circle(r)
            self.assertAlmostEqual(circle.area(), math.pi * r * r)
            
    def test_string_representation(self):
        """Test __str__ methods of all shapes"""
        from shapes.circle import Circle
        circle = Circle(2)
        self.assertEqual(str(circle), "Circle with radius 2 and area 12.566370614359172")

    def test_triangle_error_message(self):
        """Error message should be correct when invalid sides are given for Triangle."""
        from shapes.triangle import Triangle
        try:
            Triangle(3, 4, 10)
        except ValueError as v:
            self.assertEqual(str(v), "These sides do not form a triangle")

    def test_non_numeric_input(self):
        """Shapes should raise errors if non-numeric inputs are given."""
        for shape in self.shapes:
            with self.assertRaises(TypeError):
                instance = shape('abc')

    def test_zero_input(self):
        """Shapes should raise errors if zeros are used as inputs."""
        for shape in self.shapes:
            with self.assertRaises(ValueError):
                instance = shape(0)

    def test_large_inputs(self):
        """Shapes should be able to handle large numeric inputs without errors."""
        LARGE_VALUE = 10**6
        for shape in self.shapes:
            try:
                instance = shape(LARGE_VALUE)
                expected_area = instance.expected_area()
                actual_area = instance.area()
                self.assertAlmostEqual(actual_area, expected_area)
                expected_perimeter = instance.expected_perimeter()
                actual_perimeter = instance.perimeter()
                self.assertAlmostEqual(expected_perimeter, actual_perimeter)
            except Exception as e:
                self.fail(f"{shape.__name__} raised {e.__class__.__name__} with large input")
                
    def test_float_inputs(self):
        """Shapes should accurately calculate with floating point numeric inputs."""
        import math
        FLOAT_VALUE = math.pi
        for shape in self.shapes:
            try:
                instance = shape(FLOAT_VALUE)
                expected_area = instance.expected_area()
                actual_area = instance.area()
                self.assertAlmostEqual(actual_area, expected_area)
                expected_perimeter = instance.expected_perimeter()
                actual_perimeter = instance.perimeter()
                self.assertAlmostEqual(expected_perimeter, actual_perimeter)
            except Exception as e:
                self.fail(f"{shape.__name__} raised {e.__class__.__name__} with float input")
                
    def test_right_triangles(self):
        """Verify recognition of right triangles."""
        from shapes.triangle import Triangle

        for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17)]: # known triplets
            triangle = Triangle(a, b, c)
            self.assertTrue(triangle.is_right_triangle())

        for a, b, c in [(3, 4, 6), (6, 8, 11), (7, 9, 11)]: # not right triangles
            triangle = Triangle(a, b, c)
            self.assertFalse(triangle.is_right_triangle())

if __name__ == "__main__":
    unittest.main()