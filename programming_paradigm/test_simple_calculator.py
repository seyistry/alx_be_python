import unittest
from simple_calculator import SimpleCalculator


class Test_simple_calculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, 1), -1)
        self.assertEqual(self.calc.add(0, -1), -1)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_division_function(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(5, 0), None)

        


if __name__ == "__main__":
    unittest.main()
