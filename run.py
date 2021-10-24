#!/usr/bin/env python3.8
# from termcolor import colored
# import pyautogui
from user import Users
from credentials import Credentials
def function():
	print("               ____                         _____  _                               ")
	print("              |  _ \                       / ____|| |                              ")
	print("              | |_) )  ____  ___   ___    / ____  | |__    _____  _ _  ____        ")
	print("              |  __/  / _  |/ __  / __    \___  \ |  __)  /  _  \| '_|/ __ \       ")
	print("              | |    / (_| |\__ \ \__ \    ___  / | |___ (  (_)  ) | |  ___/       ")
	print("              |_|    \_____| ___/  ___/   |____/  |_____) \_____/|_|  \____        ")
function()
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
def auto_generate_password(passwordlength):
    '''
    Function that autogenerates a password of the required length.
    '''
    auto_password = Credentials.autogenerate_password(passwordlength)
    return auto_password
##################################################################################################
# The main function begins here
def main():
    print ('Hello There! Welcome to the Safest Password Locker', 'red')
    print("\n")
    while True:
        print("Use the following short-code commands for easy navigation")
        print("lg --------------> Login")
        print("EX --------------> Exit application")

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
                print("\n")
                
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
            # else:
            #     print("I really did not get that. Please use Y/N")
                
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
                        shortcode = input().upper().strip()
                        print("\n")
                        if shortcode == "CC":
                            print("Create a login credential")
                            print("-"*25)
                            
                            print("Platform name")
                            print("-"*13)
                            platform = input()
                            print("\n")
                            
                            print("Login Username/Email")
                            print("-"*20)
                            login_username = input()
                            print("\n")
                            
                            print("Login Password")
                            print("-"*14)
                            
                            print("Would you like to creat your own password or would you like to auto-generate one?")
                            print("CP ========================> Create Password")
                            print("AG ========================> Auto-Generate")
                            while True:
                                option = input().upper().strip()
                                if option == "CP":
                                    print("Create a password")
                                    print("-"*15)
                                    login_password = input()
                                    print("Press enter to continue")
                                elif option == "AG":
                                    passwordlength = int(input("Please enter the Desired password Length: \n"))
                                    login_password = auto_generate_password(passwordlength)
                                    print(f"Your auto-generated password is: {login_password} \n Press 'Enter' to continue")
                                    # break
                                else:
                                    print("I really did not get that. please use the instructed shortcodes.")
                                    # break
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
                                    print(f"Platform Name: {credential.platform}      Username: {credential.login_username}      Password: {credential.login_password}")
                            else:
                                print("You dont seem to have any credentials saved yet")
                                print("\n")
                                
                        elif shortcode == "SC":
                            print("Enter the name of the platform you wish to search for")
                            print("\n")
                            search_platform = input()
                            if check_existing_credentials(search_platform):
                                search_credential = find_credential(search_platform)
                                print("Here is the login credential you are searching for")
                                print("-"*45)
                                print(f"Platform name: {search_credential.platform}      Login Username/email: {search_credential.login_username}      Login password: {search_credential.login_password}")
                                
                            else:
                                print(f"Credentials for {search_platform} are yet to be created")
                                print("\n")
                                
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
        else:
            print("I really did not get that. Please use the given short codes")
            print("\n")
                        

if __name__ == '__main__':
    main()
                    