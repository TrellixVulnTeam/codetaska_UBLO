from codetaska import User
import unittest

user = '{ "id": 1, "username": "username", "firstName": "firstname", "lastName": "lastname", "email": "email", "password": "password", "phone": "phone", "userStatus": 0 }'


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_create_user(self):
        self.assertEqual(self.user.create(data=user), 200)

    def test_read_user(self):
        self.assertEqual(self.user.read(), 200)

    def test_update_user(self):
        self.assertEqual(self.user.update(data=user), 200)

    def test_zdelete_user(self):
        self.assertEqual(self.user.delete(), 200)

    def test_login_user(self):
        self.assertEqual(self.user.login(), 200)

    def test_logout_user(self):
        self.assertEqual(self.user.logout(), 200)


if __name__ == "__main__":
    unittest.main()
