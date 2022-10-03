import sys
import unittest
 
class LinuxTests(unittest.TestCase):
 
    def test_linux_feature(self):
        if not sys.platform.startswith("linux"):
            self.skipTest("Test only runs on Linux")
        print("I am testing...")

unittest.main()