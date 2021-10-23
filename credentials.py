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