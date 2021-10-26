import unittest #testing module
import pyperclip
from credentials import Credential
class TestCredentials(unittest.TestCase):
    """
    Test class for credentials
    Args:
    unittest.TestCase: Testcase class that helps in creating tests
    """
    def setUp(self):
        self.new_credentials = Credential("james@email.com", "facebook", 1234567)

    def test_init(self):
        self.assertEqual(self.new_credentials.email, "james@email.com")
        self.assertEqual(self.new_credentials.platform, "facebook")
        self.assertEqual(self.new_credentials.password, 1234567)

if __name__ == "__main__":
    unittest.main()