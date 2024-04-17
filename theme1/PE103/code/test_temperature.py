import unittest

from temperature import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_conversion(self):
        # Test conversion for 0°C
        self.assertEqual(celsius_to_fahrenheit(0), 32)

        # Test conversion for 100°C
        self.assertEqual(celsius_to_fahrenheit(100), 212)

        # Test conversion for negative temperature -10°C
        self.assertEqual(celsius_to_fahrenheit(-10), 14)

    def test_conversion_bad(self):
        # Test with bad input
        self.assertEqual(celsius_to_fahrenheit("not temperature"), 0)

    def test_conversion_bad_expect_exception(self):
        # Test with bad input
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit("not temperature")


if __name__ == "__main__":
    unittest.main()
