#!/usr/bin/env python3.8
from user import User
from credentials import Credential

def create_user(fname,lname,phone,email,password):

    new_user = User(fname,lname,phone,email,password)
    return new_user

def create_credential(email,platform,password):

    new_credential =  Credential(email,platform,password)
    return new_credential

def generate_password():
    '''
    Function to genrate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def save_users(user):

    user.save_user()

def save_credential(credential):

    credential.save_credential()

def del_user(user):

    user.delete_user()

def delete_credential(credential):

    credential.delete_credential()

def find_user(number):

    return User.find_by_number(number)

def find_credential(number):

    return Credential.find_by_email(number)

def check_existing_users(number):

    return User.user_exist(number)

def check_existing_credential(number):

    return Credential.credential_exist(number)

def display_users():

    return User.display_users()

def display_credential():

    return Credential.display_credential()

def test_copy_email():

    return User.copy_email()

def test_copy_email():

    return Credential.copy_email()


def main():

    print("Welcome to your contact list")
    print('\n')
    print("what is your full name")

    user_name = input()

    print(f"Hello {user_name}. What would you like to do")

    print('\n')

    while True:

        print("Use these short codes :")
        print("CU - Create a New User")
        print("FI - Find a User")
        print("DS - Display Users")       
        print("CA - Create Social Account")
        print("DA - Display Social Account")
        print("DE - Delete Social Account")
        print("EX - Exit the list")
        print("CP - for any complains")
        print("use the above short codes to navigate through the contact directory")


        short_code = input().lower()

        if short_code == 'cu':

            print("New User")
            print("-"*10)

            print ("First name .....")
            f_name = input()

            print("Last name ....")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("your Password .....")
            e_pass = input()

            save_users(create_user(f_name,l_name,p_number,e_address,e_pass))

            print('\n')

            print(f"New User {f_name} {l_name} created")

            print ('\n')

        elif short_code == 'dis':
            if display_users():

                print("Here is a list of all users")

                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                print('\n')

            else:

                print('\n')

                print(" hmmmmm....You seem not to have any users saved yet")

                print('\n')

        elif short_code == 'fu':

            print("Enter the  user's number you searching  for")

            search_number = input()

            if check_existing_users(search_number):

                search_user = find_user(search_number)

                print(f"{search_user.first_name} {search_user.last_name}")

                print('-' *20)

                print(f"Phone number...........{search_user.phone_number}")

                print(f"Email address .........{search_user.email}")

            else:

                print("That user does not exist")

        elif short_code == 'ca':

                print("Do you want password to auto-generate..use below options")
                print("Option 1: YY -- Yes")
                print("Option 2: NN -- No")
                print("Option 3: EX -- Exit the Social Acounts")

                pass_auto = input().lower()

                if pass_auto == 'yy':
                    print("Password will be auto generated")
                    print("Enter Email Address (Username).....")
                    e_mail = input()

                    print("Platform Account (Social Account)...")
                    p_account = input()

                    print("Enter Password....")
                    p_word = generate_password()

                    save_credential(create_credential(e_mail,p_account,p_word))

                    print ('\n')

                    print(f" New Credential for {e_mail} {p_account} created. Password is {p_word}")

                    print ('\n')

                elif pass_auto == 'nn':

                    print ("Enter Email Address (Username)....")
                    e_mail = input()


                    print("Platform Account (Social Account)....")
                    p_account = input()

                    print("Enter Password......")
                    p_word = input()

                    save_credential(create_credential(e_mail,p_account,p_word))


                    print ('\n')

                    print(f" New Credential for {e_mail} {p_account} created")

                    print('\n')

                elif pass_auto == "ex":

                    print("Bye ........")

                else:
                    print("Invalid option..please try again")

                    print("Do you want password to auto-generate ..use below options")

                    print("Option 1: YY -- Yes")
                    print("Option 2: NN -- No")
                    print("Option 3: EX -- Exit the social Account")

                    pass_auto = input().lower()

        elif short_code == 'da':

            if display_credential():
                print("Here is a list of all your credentials")

                print('\n')

                for credential in display_credential():

                        print(f"{credential.email} {credential.platform} .....{credential.password}")
                        print('\n')

            else:

                print('\n')

                print("You don't seem to have any credentials saved yet")
                print("input  'back' to go back" ) 
                input()
                
                input("")

                print('\n')


                if input == "back":

                 print(
        print("Use these short codes :"),
        print("CU - Create a New User"),
        print("FI - Find a User"),
        print("DS - Display Users"),       
        print("CA - Create Social Account"),
        print("DA - Display Social Account"),
        print("DE - Delete Social Account"),
        print("EX - Exit the list"),
        print("CP - for any complains"),
        print("use the above short codes to navigate through the contact directory")
)

        elif short_code == "de":

            print("Starting to delete .......")
            print("Enter Email .......")
            del_name = input(" ")

            delete_credential(del_name)

        elif short_code == "ex":

            print("Tuko pamoja!!!...good day...byee.......")

            break

        else:

            print("hmmmmm.invalid option. Please select your option from the short codes")


        if short_code =="cp":
            print("input your complains doen below")
            print("\n")
            input("state your complaint" (""))


        elif input (len) == 4:
            print("complaint recived")


        else:
            print(" please input a valid complaint")





    


if __name__ == '__main__':

    main()