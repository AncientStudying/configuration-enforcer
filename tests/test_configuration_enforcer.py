import unittest
from configuration_enforcer.configuration_enforcer import ConfigurationEnforcer


class TestConfigurationEnforcer(unittest.TestCase):
    def test_something(self):
        ce = ConfigurationEnforcer()
        self.assertEqual(True, ce.isInitialized)  # add assertion here


if __name__ == '__main__':
    unittest.main()
