#myballs

'''
User Story 1: User Registration
As a new user, I want to be able to register for a new account
using user email and password

User Story 2: Login
As a registered user, I want to be able to log into my account
using email and password

User Story 3: Password Reset
As a user who forgot their password, I want to be able ot request a password reset.
'''


import unittest
#from User import UserManagment       #Showing that you can import another file to get another class

class UserManagment():
    pass

class TestUserManagment(unittest.TestCase):
    def test_managment(self):
        #making the classes n shiz
        userManager = UserManagment() #When written, UserManagment has not been defined yet
        result = userManager.register("a@b.com","password")
        self.assertTrue(result)

    def test_login(self):
        userManager = UserManagment()
        userManager.register("a@b.com", "password")
        result = userManager.login("a@b.com", "password")
        self.assertTrue(result)
    def test_passwordReset(self):
        userManager = UserManagment()
        result = userManager.request_password_rest("a@b.com")
        self.assertTrue(result)
    def test_password_actually_rest(self):
        userManager = UserManagment()
        userManager.register("a@b.com","password")
        reset_token = userManager.request_password_rest("a@b.com")
        result = userManager.reset_password("a@b.com", reset_token,"newPassword")
        self.assertTrue(result)



        #After this line, it was from me
    def UserManagment(self, username, password):
        pass
