class Users:
    '''
    Class that generates a new instance of a user
    '''
    user_list = []
    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for the user object.
        Args:
            username: New user's username
            password: User's password for loging in to the application
        '''
        self.username = username
        self.password = password