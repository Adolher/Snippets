import unittest

def plus_one(x):
    return x+1
result_list = [-4, 1, 6]

class TestPlusOne(unittest.TestCase):
    def test_five_plus_one(self):
        self.assertIn(plus_one(5), result_list, f"Expected plus_one(5) to return 6.")
    def test_minusfive_plus_one(self):
        self.assertIn(plus_one(-5), result_list, f"Expected plus_one(-5) to return -4.")
    def test_zero_plus_one(self):
        self.assertIn(plus_one(0), result_list, f"Expected plus_one(0) to return 1.")

unittest.main()