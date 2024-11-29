import unittest
from shapes import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        # Test data preparation
        self.test_position = (1.0, 2.0, 3.0)
        self.point = Point(self.test_position)

    def test_initialization(self):
        """Test of correct initialization of Point object"""
        self.assertIsInstance(self.point, Point)
        self.assertEqual(self.point._position, self.test_position)

    def test_position_property(self):
        """Test property position returns correct coordinates"""
        self.assertEqual(self.point.position, self.test_position)
        self.assertIsInstance(self.point.position, tuple)
        self.assertEqual(len(self.point.position), 3)

    def test_immutability(self):
        """Test that position returns a new object and is immutability-protected"""
        original_position = self.point.position
        position_copy = self.point.position

        self.assertIs(self.point._position, original_position)  # Проверяем, что это тот же объект
        self.assertEqual(position_copy, original_position)  # Проверяем равенство значений

    def test_with_integer_values(self):
        """Test working with integer coordinates"""
        integer_point = Point((1, 2, 3))
        self.assertEqual(integer_point.position, (1, 2, 3))

    def test_with_negative_values(self):
        """Test working with negative coordinates"""
        negative_point = Point((-1.5, -2.5, -3.5))
        self.assertEqual(negative_point.position, (-1.5, -2.5, -3.5))

    def test_with_zero_values(self):
        """Test working with zero coordinates"""
        zero_point = Point((0.0, 0.0, 0.0))
        self.assertEqual(zero_point.position, (0.0, 0.0, 0.0))

    def test_valid_point_creation(self):
        """Test successful point creation with valid coordinates."""
        point = Point((1.0, 2.0, 3.0))
        self.assertEqual(point.position, (1.0, 2.0, 3.0))

    def test_raise_type_error_non_tuple_input(self):
        """Test TypeError is raised when input is not a tuple or list."""
        with self.assertRaises(TypeError) as context:
            Point(123)
        self.assertTrue("First argument must be a point tuple" in str(context.exception))

    def test_raise_type_error_string_input(self):
        """Test TypeError is raised when input is a string."""
        with self.assertRaises(TypeError) as context:
            Point("not a tuple")
        self.assertTrue("First argument must be a point tuple" in str(context.exception))

    def test_raise_value_error_incorrect_tuple_length(self):
        """Test ValueError is raised when tuple does not have exactly 3 coordinates."""
        with self.assertRaises(ValueError) as context:
            Point((1.0, 2.0))
        self.assertTrue("Points must have exactly 3 coordinates" in str(context.exception))

    def test_raise_value_error_four_coordinate_tuple(self):
        """Test ValueError is raised when tuple has more than 3 coordinates."""
        with self.assertRaises(ValueError) as context:
            Point((1.0, 2.0, 3.0, 4.0))
        self.assertTrue("Points must have exactly 3 coordinates" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
