import unittest
from appDB import delete_database
from users.data import UsersDB
from tests.init_test_database import init_test_database
from utils.constants import TEST_DATABASE_PATH
from users.models import User


class UsersDatabaseTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_test_database(TEST_DATABASE_PATH)

    @classmethod
    def tearDownClass(cls):
        delete_database(TEST_DATABASE_PATH)

    def setUp(self):
        self.database = UsersDB(TEST_DATABASE_PATH)

    def test_create_user(self):
        user = User(username='test_user5')
        retrieved_user = self.database.create_user(user)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'test_user5')

    def test_get_user(self):
        retrieved_user = self.database.get_user(1)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'test_user')

    def test_update_user(self):
        user = User(userid=2, username='new_test_user')
        retrieved_user = self.database.update_user(user)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, 'new_test_user')

    def test_delete_user(self):
        answer = self.database.delete_user(3)
        self.assertIsNotNone(answer)
        self.assertEqual(answer, True)

    def test_get_all_users(self):
        res = self.database.get_all_users()
        self.assertIsNotNone(res)
        self.assertEqual(len(res), 3)


if __name__ == '__main__':
    unittest.main()
