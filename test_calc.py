import unittest
import calc

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        assert 4 == calc.add(2, 2)

    def test_subtraction(self):
        assert 2 == calc.subtract(4, 2)

if __name__ == '__main__':
    unittest.main()