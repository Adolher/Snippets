import unittest

def rais(x):
    if x <= 27:
        raise ValueError
    else:
        return x

class TestRais(unittest.TestCase):
    def test_1(self):
        self.assertRaises(ValueError, rais, 1)
    def test_1984(self):
        self.assertRaises(ValueError, rais, 1984)
    def test_17(self):
        self.assertRaises(ValueError, rais, 27)

unittest.main()