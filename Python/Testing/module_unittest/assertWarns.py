import unittest
import warnings

class LeverWarning(Warning):
    pass

def rais(x):
    if x < 27:
        warnings.warn("Level under 27", LeverWarning)
    else:
        return x

class TestRais(unittest.TestCase):
    def test_1(self):
        self.assertWarns(LeverWarning, rais, 1)
    def test_1984(self):
        self.assertWarns(LeverWarning, rais, 1984)
    def test_17(self):
        self.assertWarns(LeverWarning, rais, 26)

unittest.main()