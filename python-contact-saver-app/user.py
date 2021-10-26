import pyperclip 
class User:
    """
    Class that generates new instances of users.
    """
    user_list = [] #empty user lists

    def save_user(self):

        User.user_list.append(self)

    def delete_user(self):
        """
        function to remove user
        """
        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,number):
        """
        Check if user exists
        """
        for user in cls.user_list:
            if user.phone_number == number:
                return True
        return False

    @classmethod
    def find_by_number(cls,number):
        """
        method to search user by phone number
        """
        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def display_users(cls):
        """
        Method to display all users
        """
        return cls.user_list

    @classmethod
    def copy_email(cls,number):
        """
        Method to copy user email
        """
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)



    def __init__(self,first_name,last_name,phone_number,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password