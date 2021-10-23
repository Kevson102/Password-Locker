#!/usr/bin/env python3.8
from user import Users

def register_user(username, password):
    '''
    Function that creates a new user.
    '''
    new_user = Users(username, password)
    return new_user

def save_user(user_log):
    '''
    Function that saves the user record.
    '''
    user_log.save_user()
    
def delete_user(user_log):
    '''
    Function that deletes a user
    '''
    user_log.delete_user()
    
def check_existing_users(username, password):
    '''
    Function that checks if a contact exists with the username and password and returns a boolean
    '''
    return Users.user_exist(username, password)

##################################################################################################
# The main function begins here
# from goto import goto, label
def main():
    print("Hello There! Welcome to the Safest Password Locker")
    print("\n")
    print("\n")
    while True:
        # label .nowLogin
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
                
                # goto .nowLogin #Switches the user back to the login section
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
                else:
                    print("Login Successful")

if __name__ == '__main__':
    main()
                    