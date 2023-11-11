import unittest

from appDB import delete_database
from tasks import Task
from tests.init_test_database import init_test_database
from utils.constants import TEST_DATABASE
from tasks.data import TaskDB


class TasksDatabaseTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_test_database(TEST_DATABASE)

    @classmethod
    def tearDownClass(cls):
        delete_database(TEST_DATABASE)

    def setUp(self):
        self.database = TaskDB(TEST_DATABASE)

    def test_create_task(self):
        task = Task(username='new_test_user', title='new_title', description='new_desc', done=True)
        retrieved_task = self.database.create_task(task)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.username, 'new_test_user')
        self.assertEqual(retrieved_task.title, 'new_title')
        self.assertEqual(retrieved_task.description, 'new_desc')
        self.assertEqual(retrieved_task.done, 'True')

    def test_get_task(self):
        retrieved_task = self.database.get_task(1)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.username, 'test_user')
        self.assertEqual(retrieved_task.title, 'test_title')
        self.assertEqual(retrieved_task.description, 'test_description')
        self.assertEqual(retrieved_task.done, 'False')

    def test_update_task(self):
        task = Task(taskid=2, username='new_test_user1', title='new_title1', description='new_desc1', done=True)
        retrieved_task = self.database.update_task(task)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.username, 'new_test_user1')
        self.assertEqual(retrieved_task.title, 'new_title1')
        self.assertEqual(retrieved_task.description, 'new_desc1')
        self.assertEqual(retrieved_task.done, 1)

    def test_delete_task(self):
        answer = self.database.delete_task(3)
        self.assertIsNotNone(answer)
        self.assertEqual(answer, True)

    def test_get_all_task(self):
        answer = self.database.get_all_user_tasks('test_user')
        self.assertIsNotNone(answer)
        self.assertEqual(len(answer), 2)


if __name__ == '__main__':
    unittest.main()
