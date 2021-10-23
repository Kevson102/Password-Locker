class Credentials:
    '''
    Class that generates a new instance of login credentials
    '''
    credential_list = []
    def __init__(self, platform, login_username, login_password):
        '''
        __init__ method that helps use define the properties for a credential object.
        Args:
            platform: The name of the platform whose login is being registered e.g. Twitter
            login_username: The username used to login into the platform
            login_password: The password for the platform account
        '''
        self.platform = platform
        self.login_username = login_username
        self.login_password = login_password
        
    def save_credential(self):
        '''
        This method saves the credential object in the credential_list.
        '''
        Credentials.credential_list.append(self)
        
    def delete_credential(self):
        '''
        Method that deletes a saved login credential from the credential list.
        '''
        Credentials.credential_list.remove(self)
        
    @classmethod
    def credential_exist(cls, platform):
        '''
        Method for checking if a credential exists in the credentials list.
        Args:
            platform: The online platform for which we need credentials for
        Returns:
            Boolean: True or False depending on whether the credential exists.
        '''
        for credential in cls.credential_list:
            if credential.platform == platform:
                return True
        return False