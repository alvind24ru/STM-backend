import os
import tempfile
import unittest
from unittest import TestCase

import appDB
from main import app
import flask
from tasks.data import TaskDB
from users.data import UsersDB
from utils.constants import TEST_DATABASE_PATH, DATABASE_PATH


class UsersTests(TestCase):

    @classmethod
    def setUpClass(cls):
        app.testing = True
        app.config['DATABASE_URL'] = TEST_DATABASE_PATH
        appDB.init_database(app.config['DATABASE_URL'])

    @classmethod
    def tearDownClass(cls):
        appDB.drop_all(app.config['DATABASE_URL'])
        app.testing = False
        app.config['DATABASE_URL'] = DATABASE_PATH

    def setUp(self):
        self.app = app.test_client()

    def test_test(self):
        with self.app as client:
            response = client.get('/test')
            self.assertEqual(response.text, "True")

    def test_create_user(self):
        with self.app as client:
            response = client.post('/api/v0.1.0/users?username=testuser1')
            print(response.text)
            self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        with self.app as client:
            response = client.get('/api/v0.1.0/users/4')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
