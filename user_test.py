import unittest # imports the unittest module
from user import Users # imports the users class from the user.py file

class TestUsers(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the Users class.
    Args:
        unittest.TestCase: Test case class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Setup method to run before each test case.
        '''
        self.new_user = Users("Kevson", "CsGitituComp")
    
    def test_init(self):
        '''
        This test checks whether the object is initialized properly.
        '''
        self.assertEqual(self.new_user.username, "Kevson")
        self.assertEqual(self.new_user.password, "CsGitituComp")
        
    if __name__ == '__main__':
        unittest.main()