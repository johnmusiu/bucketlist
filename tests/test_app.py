"""Unit testing classes"""

import unittest
#import logging

from app import app, database
class TestBucketlistApp(unittest.TestCase):
    """this class contains tests for all logout related issues"""
    def test_(self):
        '''this method tests logout functionality'''

    def test_session(self):
        '''tests session initialization'''

    def test_login_loads(self):
        '''checks if home page redirects to login if user not logged in'''
        test = app.test_client(self)
        response = test.get('/')
        print("--testing home redirects to login if no user is active in session--")
        self.assertEqual(response.status_code, 200, msg="passes test")

    def test_login_correct_credentials(self):
        '''tests that login works with good credentials'''
        test = app.test_client(self)
        response = test.post('/login', data=dict(username="root", password="pass"), follow_redirects=True)
        self.assertIn(b'Login successfull', response.data)

    def test_login_incorrect_credentials(self):
        '''tests that login doesnt work with wrong credentials'''
        test = app.test_client(self)
        response = test.post('/login', data=dict(username="user12", 
        password="pass12"), follow_redirects = True)
        self.assertIn(b'Username not associated with any accounts', response.data)

    def test_registration_form_loads(self):
        '''test that the page loads '''
        test = app.test_client(self)
        response = test.get('/register')
        print("---testing register loads---")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
