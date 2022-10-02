import unittest

def plus_one(x):
    return x+2

class TestPlusOne(unittest.TestCase):
    def test_five_plus_one(self):
        self.assertEqual(plus_one(5), 6, f"Expected plus_one(5) to return 6.")
    def test_minusfive_plus_one(self):
        self.assertEqual(plus_one(-5), -4, f"Expected plus_one(-5) to return -4.")
    def test_zero_plus_one(self):
        self.assertEqual(plus_one(0), 1, f"Expected plus_one(0) to return 1.")

unittest.main()