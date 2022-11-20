import sys
import unittest
 
class WindowsTests(unittest.TestCase):
 
    @unittest.skipUnless(sys.platform.startswith("win"), "This test only runs on Windows")
    def test_linux_feature(self):
        print("This test should only run on Windows")
 
    @unittest.skipIf(sys.platform.startswith("win"), "This test only runs on Linux")
    def test_other_linux_feature(self):
        print("This test should only run on Linux")

unittest.main()