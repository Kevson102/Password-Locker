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
        
    def save_user(self):
        '''
        save user method for saving the users object in the user_list
        '''
        Users.user_list.append(self)
        
    def delete_user(self):
        '''
        Method deletes a saved user from the user_list
        '''
        Users.user_list.remove(self)