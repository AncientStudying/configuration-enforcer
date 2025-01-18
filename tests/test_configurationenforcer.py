import unittest
from configurationenforcer.configurationenforcer import ConfigurationEnforcer

class MyTestCase(unittest.TestCase):
    def test_something(self):
        ce = ConfigurationEnforcer()
        self.assertEqual(True, ce.isInitialized)  # add assertion here


if __name__ == '__main__':
    unittest.main()
