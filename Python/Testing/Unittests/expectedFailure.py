import unittest

class FeatureTests(unittest.TestCase):
 
    @unittest.expectedFailure
    def test_broken_feature(self):
        raise Exception("This test is going to fail")

    def test_feature(self):
        print("This test is OK")


unittest.main()