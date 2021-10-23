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

        short_code = input().upper()
        print("\n")
        if short_code == "LG":
            print("Do you have an account? (y/n)")

            account_status = input().upper().strip()
            if account_status == "N":
                print("Please create an account to login and use the application")
                print("\n")
                
                print("Username")
                print("-"*8)
                username = input()
                print("\n")
                
                print("Password")
                print("-"*8)
                password = input()
                print("\n")
                
                save_user(register_user(username, password)) # Creates and saves the user login record
                print("Account created successfully")
                
            else:
                print("Login with you credentials")
                print("\n")
                
                print("Username")
                print("-"*8)
                username = input()
                print("\n")
                
                print("Password")
                print("-"*8)
                password = input()
                print("\n")
                if check_existing_users(username, password) == False:
                    print("Incorrect username or password.")
                    print("\n")
                    print("\n")
                    # break
                else:
                    print("Login Successful")
                    while True:
                        print("\n")
                        print("use the following short-codes to navigate through the application")
                        print("CC   ====================> Create a new Credential")
                        print("sc   ====================> Search for platform Credential")
                        print("DC   ====================> Display all Credentials")
                        print("DelC ====================> Delete a Credential")
                        print("LO   ====================> Log Out")
                        print("\n")
                        print("What would you like to do? Please use the short-codes provided above.")
                        shortcode = input().upper()
                        print("\n")
                        if shortcode == "CC":
                            print("Create a login credential")
                            print("-"*25)
                            
                            print("Platform name")
                            print("-"*13)
                            platform = input()
                            print("\n")
                            
                            print("Login Username/Email")
                            print("-"*14)
                            login_username = input()
                            print("\n")
                            
                            print("Login Password")
                            print("-"*14)
                            login_password = input()
                            print("\n")
                            
                            save_credential(add_credential(platform, login_username, login_password))
                            print("\n")
                            print(f"Login credentials for your {platform} account have been created and saved.")
                            
                        elif shortcode == "DC":
                            if display_all_saved_credentials():
                                print("Here is a list of all credentials in storage")
                                print("-"*45)
                                print("\n")
                                for credential in display_all_saved_credentials():
                                    print(f"Platform Name: {credential.platform}...Username: {credential.login_username}...Password{credential.login_password}")
                            else:
                                print("You dont seem to have any credentials saved yet")
                                print("\n")
                                
                        elif shortcode == "SC":
                            print("Enter the name of the platform you wish to search for")
                            search_platform = input()
                            if check_existing_credentials(search_platform):
                                search_credential = find_credential(search_platform)
                                print("Here is the credential you are searching for")
                                print("-"*45)
                                print(f"{search_credential.platform} {search_credential.login_username} {search_credential.login_password}")
                            else:
                                print(f"Credentials for {search_platform} are yet to be created")
                                
                        elif shortcode == "DELC":
                            print("Enter the name of the platform whose credentials you wish to delete")
                            delete_data = input()
                            if check_existing_credentials(delete_data):
                                to_delete = find_credential(delete_data)
                                to_delete.delete_credential()
                                print(f"The login credentials for {delete_data} have been deleted")
                                print("\n")
                                #print("Please confirm your delete request")
                            else:
                                print("No such credential exists in memory")
                        
                        elif shortcode == "LO":
                            print("Thank you for using password locker. See you next time")
                            break
                        else:
                            print("I really did not get that. Please use the indicated short codes")
                            
                            
        elif short_code == "EX":              
            print("Good Bye.....")
            break
                        

if __name__ == '__main__':
    main()
                    