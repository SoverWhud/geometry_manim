import unittest
from manim import *
from scenes import CreateNumberPlane


class NumberPlaneTest(unittest.TestCase):
    def test_scene_creation(self):
        """Test basic scene creation and configuration"""
        scene = CreateNumberPlane()
        self.assertIsInstance(scene, CreateNumberPlane)
        self.assertIsInstance(scene, Scene)

    def test_number_plane_configuration(self):
        """Test NumberPlane configuration details"""
        scene = CreateNumberPlane()
        scene.render()  # Simulate scene rendering

        # Verify plane exists
        plane = scene.mobjects[0]
        self.assertIsInstance(plane, NumberPlane)

        # Test screen dimension calculations
        self.assertEqual(plane.x_range[0],  -config.frame_width / 2)
        self.assertEqual(plane.x_range[1],  config.frame_width / 2)
        self.assertEqual(plane.y_range[0],  -config.frame_height / 2)
        self.assertEqual(plane.y_range[1],  config.frame_height / 2)

    def test_line_style(self):
        """Test line style configuration"""
        scene = CreateNumberPlane()
        scene.render()

        plane = scene.mobjects[0]
        line_style = plane.background_line_style

        self.assertEqual(line_style['stroke_color'],  TEAL)
        self.assertEqual(line_style['stroke_width'],  4)
        self.assertEqual(line_style['stroke_opacity'],  0.6)

    def test_plane_dimensions(self):
        """Verify plane dimensions match screen dimensions"""
        scene = CreateNumberPlane()
        scene.render()

        plane = scene.mobjects[0]
        self.assertEqual(plane.x_length,  config.frame_width)
        self.assertEqual(plane.y_length,  config.frame_height)

    def test_plane_centering(self):
        """Verify plane is centered"""
        scene = CreateNumberPlane()
        scene.render()

        plane = scene.mobjects[0]
        self.assertTrue(np.allclose(plane.get_center(), np.array([0, 0, 0])))


if __name__ =='__main__':
    unittest.main()
