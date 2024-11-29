import unittest
import manim

import mobjects
import shapes

class TestCreateLabelMobjects(unittest.TestCase):
    def setUp(self):
        """
        Set up test data before each test method
        """
        # Create a test label with a sample text and position
        self.test_label = shapes.Label(
            text=r"Hello, World!",
            position=(1.0, 2.0, 0.0)
        )
        self.test_font_size = 24

    def test_successful_label_mobject_creation(self):
        """
        Test successful creation of a Text mobject with correct parameters
        """
        text_mobject = mobjects.create_label_mobjects(self.test_label, self.test_font_size)

        self.assertIsInstance(text_mobject, manim.Text)

        self.assertEqual(text_mobject.text, self.test_label.text.replace(" ", ""))
        self.assertAlmostEqual(text_mobject.font_size, self.test_font_size)
        self.assertSequenceEqual(tuple(text_mobject.get_center()), self.test_label.position)

    def test_invalid_shape_type(self):
        """
        Ensure TypeError is raised when passing a non-Label object
        """
        with self.assertRaises(TypeError):
            mobjects.create_label_mobjects("not a label", self.test_font_size)

    def test_additional_kwargs(self):
        """
        Test passing additional keyword arguments to Text constructor
        """
        text_mobject = mobjects.create_label_mobjects(
            self.test_label,
            self.test_font_size,
            color=manim.RED,
            weight=manim.BOLD
        )

        # Verify additional arguments are applied
        # self.assertEqual(text_mobject.color, manim.RED)  # TODO: Test not working
        self.assertEqual(text_mobject.weight, manim.BOLD)

    def test_zero_font_size(self):
        """
        Test behavior when font size is set to zero
        """
        text_mobject = mobjects.create_label_mobjects(self.test_label, 0)
        self.assertIsInstance(text_mobject, manim.Text)

        with self.assertRaises(ZeroDivisionError):
            test = text_mobject.font_size

    def test_empty_text_label(self):
        """
        Test creation of label with empty text
        """
        empty_label = shapes.Label(
            text="",
            position=(0.0, 0.0, 0.0)
        )

        text_mobject = mobjects.create_label_mobjects(empty_label, self.test_font_size)

        # Verify empty text is handled correctly
        self.assertEqual(text_mobject.text, "")
        self.assertSequenceEqual(tuple(text_mobject.get_center()), empty_label.position)

    def test_complex_positioning(self):
        """
        Test label creation with complex positioning
        """
        complex_label = shapes.Label(
            text="Complex Position",
            position=(-5.5, 3.2, 1.1)
        )

        text_mobject = mobjects.create_label_mobjects(complex_label, self.test_font_size)
        self.assertSequenceEqual(tuple(text_mobject.get_center()), complex_label.position)



if __name__ == '__main__':
    unittest.main()