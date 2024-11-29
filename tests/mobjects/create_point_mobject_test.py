import unittest
import manim

import mobjects
import shapes

class TestCreatePointMobject(unittest.TestCase):
    def setUp(self):
        self.test_point = shapes.Point(position=(1.0, 2.0, 0.0))
        self.test_scale = 2.0

    def test_successful_point_mobject_creation(self):
        """
        Tests if the Manim point was successfully created with the correct parameters
        """
        dot = mobjects.create_point_mobject(self.test_point, self.test_scale)

        self.assertIsInstance(dot, manim.Dot)
        self.assertSequenceEqual(tuple(dot.get_center()), self.test_point.position)
        self.assertAlmostEqual(dot.width, manim.Dot().width * self.test_scale)

    def test_invalid_point_type(self):
        """
        Tests that the function causes a TypeError when passing an object that is not Point
        """
        with self.assertRaises(TypeError):
            mobjects.create_point_mobject("not a point", self.test_scale)

    def test_additional_kwargs(self):
        """
        Tests whether additional arguments are passed correctly
        """
        dot = mobjects.create_point_mobject(
            self.test_point,
            self.test_scale,
            color=manim.RED,
            fill_opacity=0.5
        )

        self.assertEqual(dot.color, manim.RED)
        self.assertAlmostEqual(dot.fill_opacity, 0.5)

    def test_zero_scale(self):
        """
        Tests the scaling behavior with a factor of 0
        """
        dot = mobjects.create_point_mobject(self.test_point, 0)

        self.assertAlmostEqual(dot.width, 0)

    def test_negative_scale(self):
        """
        Tests the behavior for negative scaling
        """
        dot = mobjects.create_point_mobject(self.test_point, -1)

        self.assertAlmostEqual(dot.width, manim.Dot().width)


if __name__ == '__main__':
    unittest.main()