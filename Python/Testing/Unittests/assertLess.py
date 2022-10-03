import unittest

def less_than(x, y):
    return y if x>y else x

class TestLessThen(unittest.TestCase):
    def test_one_less_than_zero(self):
        self.assertLess(less_than(1, 0), 10)
    def test_minusfive_less_than_ten(self):
        self.assertLess(less_than(-5, 10), 10)
    def test_five_less_than_five(self):
        self.assertLess(less_than(5, 5), 5)

unittest.main()
