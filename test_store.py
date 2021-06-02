from codetaska import Store
import unittest

order = '{ "id": 1, "petId": 1, "quantity": 0, "shipDate": "2021-06-01T23:32:58.235Z", "status": "placed", "complete": true }'


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()

    def test_read_inventory(self):
        self.assertEqual(self.store.read_inventory(), 200)

    def test_create_order(self):
        self.assertEqual(self.store.create_order(data=order), 200)

    def test_read_order(self):
        self.assertEqual(self.store.read_order(), 200)

    def test_zdelete_order(self):
        self.assertEqual(self.store.delete_order(), 200)


if __name__ == "__main__":
    unittest.main()
