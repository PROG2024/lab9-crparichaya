"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest

class TestCircle(unittest.TestCase):
    def test_area_with_typical_case(self):
        """Test add_area with two circles having positive radii"""
        circle1 = Circle(3)
        circle2 = Circle(4)
        result = circle1.add_area(circle2)

        self.assertEqual(result.get_radius(), 5)

    def test_area_with_edge_case(self):
        """Test when one of the circles has radius 0, the other has non-zero radius.
        (Result should have same radius.)  """
        circle1 = Circle(0)
        circle2 = Circle(4)
        result  =circle1.add_area(circle2)

        self.assertEqual(result.get_radius(), 4)

    def test_radius_cannot_be_negative(self):
        """Test the redius if radius is negative if will raise error"""
        with self.assertRaises(ValueError):
            Circle(-1)



