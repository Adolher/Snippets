import unittest

def less_than(x, y):
    return True if x>y else False

class TestLessThen(unittest.TestCase):
    def test_one_less_than_zero(self):
        self.assertTrue(less_than(1, 0))
    def test_minusfive_less_than_ten(self):
        self.assertTrue(less_than(-5, 10))
    def test_five_less_than_five(self):
        self.assertTrue(less_than(5, 5))

unittest.main()