import unittest

def power_cycle_device():
    print('Power cycling bluetooth device...')
def check_for_each_test():
    print("short check...")
 
class BluetoothDeviceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        power_cycle_device()

    def setUp(self):
        check_for_each_test()
 
    def test_feature_a(self):
        print('Testing Feature A')
 
    def test_feature_b(self):
        print('Testing Feature B')
 
    @classmethod
    def tearDownClass(cls):
        power_cycle_device()

unittest.main()