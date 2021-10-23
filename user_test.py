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
        
    def tearDown(self):
        '''
        Method that cleans up after every test case
        '''
        Users.user_list = []
    
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
        
    def test_delete_user(self):
        '''
        Test for checking if we can remove a user from the list
        '''
        self.new_user.save_user()
        test_user = Users("Josephine", "2563254") #New user registered
        test_user.save_user()
        
        self.new_user.delete_user() #Deleting a User
        self.assertEqual(len(Users.user_list),1)
        
    def test_user_exists(self):
        '''
        Test if we can return a boolean depending on whether we find a user in the list or not
        '''
        self.new_user.save_user()
        test_user = Users("Josephine", "2563254") #New user registered
        test_user.save_user()
        
        user_exists = Users.user_exist("Josephine","2563254")
        self.assertTrue(user_exists)
        
        
        
    if __name__ == '__main__':
        unittest.main()