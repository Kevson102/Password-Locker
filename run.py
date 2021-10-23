#!/usr/bin/env python3.8
from user import Users
from credentials import Credentials

def register_user(username, password):
    '''
    Function that creates a new user.
    '''
    new_user = Users(username, password)
    return new_user

def add_credential(platform, login_username, login_password):
    '''
    Function that creates a new login credential.
    '''
    new_credential = Credentials(platform, login_username, login_password)
    return new_credential

def save_user(user_log):
    '''
    Function that saves the user record.
    '''
    user_log.save_user()
    
def save_credential(login_credential):
    '''
    Function that saves new credentials.
    '''
    login_credential.save_credential()
    
def delete_user(user_log):
    '''
    Function that deletes a user
    '''
    user_log.delete_user()
    
def delete_credential(login_credential):
    '''
    Function that deletes a credential.
    '''
    login_credential.delete_credential()
    
def check_existing_users(username, password):
    '''
    Function that checks if a contact exists with the username and password and returns a boolean
    '''
    return Users.user_exist(username, password)

def check_existing_credentials(platform):
    '''
    Function that checkes if login credentials to a platform exists and returns a boolean.
    '''
    return Credentials.credential_exist(platform)

def find_credential(platform):
    '''
    Function that finds a credential by platform and returns the login credentials.
    '''
    return Credentials.find_credential_by_platform(platform)

def display_all_saved_credentials():
    '''
    Function that displays all the saved login credentials.
    '''
    return Credentials.display_all_credentials()
##################################################################################################
# The main function begins here
def main():
    print("Hello There! Welcome to the Safest Password Locker")
    print("\n")
    print("\n")
    while True:
        print("Use the following short-code commands for easy navigation")
        print("lg -------------- Login")
        print("EX -------------- Exit application")
        print("\n")
        print("\n")
        short_code = input().upper()
        if short_code == "LG":
            print("Do you have an account? (y/n)")
            print("\n")
            print("\n")
            account_status = input().upper()
            if account_status == "N":
                print("Please create an account to use the application")
                print("\n")
                
                print("Username")
                print("-"*8)
                username = input()
                
                print("Password")
                print("-"*8)
                password = input()
                
                save_user(register_user(username, password)) # Creates and saves the user login record
                print("Account created successfully")
                
            else:
                print("Login with you credentials")
                print("\n")
                print("\n")
                
                print("Username")
                print("-"*8)
                username = input()
                print("\n")
                print("\n")
                
                print("Password")
                print("-"*8)
                password = input()
                if check_existing_users(username, password) == False:
                    print("Incorrect username or password.")
                    break
                else:
                    print("Login Successful")

if __name__ == '__main__':
    main()
                    