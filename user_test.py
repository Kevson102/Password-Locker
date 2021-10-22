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
    
    def test_save_user(self):
        '''
        test_save_user test case for testing if the user object is saved in the user list.
        '''
        self.new_user.save_user() #Saving the new user
        self.assertEqual(len(Users.user_list),1) # Checks whether the length of the user_list increases by 1 after the saving
        
    def test_save_multiple_users(self):
        '''
        Test_save _multiple_users to check if we can save multiple user objects in the user-list
        '''
        self.new_user.save_user()
        test_user = Users("Josephine", "2563254") #New user registered
        test_user.save_user()
        self.assertEqual(len(Users.user_list), 2)
        
    if __name__ == '__main__':
        unittest.main()