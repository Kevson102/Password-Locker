import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the credentials class.
    Args:
        unittest.TestCase: Test case class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Setup method that runs before each test case.
        '''
        self.new_credential = Credentials("Twitter", "@Kevson102", "MyPassword")
        
    def tearDown(self):
        '''
        Method that cleans up after every test case
        '''
        Credentials.credential_list = []
        
    def test_init(self):
        '''
        This test checks whether the credential object was initialized properly.
        '''
        self.assertEqual(self.new_credential.platform, "Twitter")
        self.assertEqual(self.new_credential.login_username, "@Kevson102")
        self.assertEqual(self.new_credential.login_password, "MyPassword")
        
    def test_save_credential(self):
        '''
        Test case for testing if the credential object can be saved in the credential list.
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)
        
    def test_save_multiple_credentials(self):
        '''
        Test case to check if we can save multiple credential objects in the credential list.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "Kevson102@gmail.com", "11223344")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list), 2)
        
    def test_delete_credential(self):
        '''
        Test case to check if we can remove a login credential from the credential list.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "Kevson102@gmail.com", "11223344")
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1)
        
    def test_credential_exists(self):
        '''
        Test case to check if a credential exist
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "Kevson102@gmail.com", "11223344")
        test_credential.save_credential()
        
        credential_exists = Credentials.credential_exist("Gmail")
        self.assertTrue(credential_exists)
        
    def test_find_credential_by_platform(self):
        '''
        Test to check if we can find a credential by platform name and display the username and password for the platform.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "Kevson102@gmail.com", "11223344")
        test_credential.save_credential()
        
        found_credential = Credentials.find_credential_by_platform("Gmail")
        self.assertEqual(found_credential.login_username, test_credential.login_username)
        
    def test_display_all_credentials(self):
        '''
        Method that returns a list of all the saved credentials.
        '''
        self.assertEqual(Credentials.display_all_credentials(),Credentials.credential_list)
        
if __name__ == '__main__':
    unittest.main()
