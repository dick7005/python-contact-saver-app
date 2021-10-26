import unittest #import the unittest testing module
from user import User #import user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating tests
    '''

    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.user_list = User("jane","doe","0734538463","janedoe@gmail.com","password")


    def test_init(self):
        """
        Test to see if the object is properly initialized
        """

        self.assertEqual(self.user_list.first_name,"jane")
        self.assertEqual(self.user_list.last_name,"doe")
        self.assertEqual(self.user_list.phone_number,"0734538463")
        self.assertEqual(self.user_list.email,"janedoe@gmail.com")
        self.assertEqual(self.user_list.password,"password")
if __name__ == '__main__':
    unittest.main()   