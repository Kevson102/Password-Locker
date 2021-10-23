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
        
if __name__ == '__main__':
    unittest.main()
