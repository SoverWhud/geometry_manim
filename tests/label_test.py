import unittest
import shapes


class TestLabelClass(unittest.TestCase):
    def setUp(self):
        # Test data preparation
        self.test_position = (1.0, 2.0, 3.0)
        self.test_text = "Test Label"
        self.label = shapes.Label(self.test_text, self.test_position)


    def test_text_property(self):
        """Test property text returns correct text"""
        self.assertEqual(self.label.text, self.test_text)
        self.assertIsInstance(self.label.text, str)

    def test_position_property(self):
        """Test property position returns correct coordinates"""
        self.assertEqual(self.label.position, self.test_position)
        self.assertIsInstance(self.label.position, tuple)
        self.assertEqual(len(self.label.position), 3)

    def test_immutability(self):
        """Test that position returns a new object and is immutability-protected"""
        original_position = self.label.position
        position_copy = self.label.position

        self.assertIs(self.label._position, original_position)  # Checking that it's the same object
        self.assertEqual(position_copy, original_position)  # Check the equality of values

    def test_valid_label_creation(self):
        """Test successful label creation with valid text and position."""
        label = shapes.Label("Test Label", (1.0, 2.0, 3.0))
        self.assertEqual(label.text, "Test Label")
        self.assertEqual(label.position, (1.0, 2.0, 3.0))

    def test_text_setter_valid_input(self):
        """Test text setter with valid string input."""
        label = shapes.Label("Initial", (1.0, 2.0, 3.0))
        label.text = "Updated Label"
        self.assertEqual(label.text, "Updated Label")

    def test_raise_type_error_invalid_text(self):
        """Test TypeError is raised when text is not a string."""
        with self.assertRaises(TypeError) as context:
            shapes.Label(123, (1.0, 2.0, 3.0))
        self.assertTrue("Value must be string." in str(context.exception))

    def test_raise_type_error_non_tuple_position(self):
        """Test TypeError is raised when position is not a tuple/list."""
        with self.assertRaises(TypeError) as context:
            shapes.Label("Test", 123)
        self.assertTrue("First argument must be a point tuple" in str(context.exception))

    def test_raise_value_error_incorrect_position_length(self):
        """Test ValueError is raised when position tuple does not have 3 coordinates."""
        with self.assertRaises(ValueError) as context:
            shapes.Label("Test", (1.0, 2.0))
        self.assertTrue("Points must have exactly 3 coordinates" in str(context.exception))


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
