import unittest

class TestLessThen(unittest.TestCase):
    def test_one_less_than_zero(self):
        self.assertAlmostEqual(2.53795597, 2.53795596)
    def test_minusfive_less_than_ten(self):
        self.assertAlmostEqual(0.1, 0.1)
    def test_five_less_than_five(self):
        self.assertAlmostEqual(2.5379551, 2.5379553)

unittest.main()
