import unittest
from unittest.mock import MagicMock

import utils

from manim import config


class TestScalingManager(unittest.TestCase):
    def setUp(self):
        """Setup test environment with saved original Manim config values"""
        self.original_frame_width = config.frame_width
        self.original_frame_height = config.frame_height

        # Set temporary test configuration
        config.frame_width = 800
        config.frame_height = 600

    def tearDown(self):
        """Restore original Manim configuration after tests"""
        config.frame_width = self.original_frame_width
        config.frame_height = self.original_frame_height

    def test_init_with_valid_scene(self):
        """Test initialization of ScalingManager"""
        scaling_manager = utils.ScalingManager(config.frame_width, config.frame_height)
        self.assertEqual(scaling_manager.frame_width, 800)
        self.assertEqual(scaling_manager.frame_height, 600)
        self.assertEqual(scaling_manager.scale, 600 / 8)

    def test_get_scaled_size(self):
        """Test scaling size relative to window size"""
        scaling_manager = utils.ScalingManager(config.frame_width, config.frame_height)

        base_size = 2.0
        expected_scaled_size = base_size * (600 / 8)
        scaled_size = scaling_manager.get_scaled_size(base_size)

        self.assertAlmostEqual(scaled_size, expected_scaled_size)

    def test_get_scaled_size_with_different_base_sizes(self):
        """Test scaling with various base sizes"""
        scaling_manager = utils.ScalingManager(config.frame_width, config.frame_height)

        test_cases = [
            (1.0, 1.0 * (600 / 8)),
            (0.5, 0.5 * (600 / 8)),
            (4.0, 4.0 * (600 / 8))
        ]

        for base_size, expected in test_cases:
            with self.subTest(base_size=base_size):
                scaled_size = scaling_manager.get_scaled_size(base_size)
                self.assertAlmostEqual(scaled_size, expected)


if __name__ == '__main__':
    unittest.main()
