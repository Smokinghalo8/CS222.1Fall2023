#myballs

'''
User Story 1: User Registration
As a new user, I want to be able to register for a new account
using user email and password

User Story 2: Login
As a registered user, I want to be able to log into my account
using email and password
'''


import unittest
#from User import UserManagment       #Showing that you can import another file to get another class

class TestUserManagment(unittest.TestCase):
    def test_managment(self):
        #making the classes n shiz
        userManager = UserManagement() #When written, UserManagment has not been defined yet
        result = userManager.register("a@b.com","password")
        self.assertTrue(result)

    def test_login(self):
        userManager = UserManagment()
        userManager.register("a@b.com", "password")
        result = userManager.login("a@b.com", "password")
        self.assertTrue(result)


        #After this line, it was from me
    def UserManagment(self, username, password):
        pass
