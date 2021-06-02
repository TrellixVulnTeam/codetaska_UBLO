import unittest
from codetaska import Pet, Store

pet = '{ "id": 1, "category": { "id": 1, "name": "string" }, "name": "doggie", "photoUrls": [ "string" ], "tags": [ { "id": 1, "name": "string" } ], "status": "available" }'


class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet()

    def test_pet_create(self):
        self.assertEqual(self.pet.create(data=pet), 200)

    def test_pet_read(self):
        self.assertEqual(self.pet.read(), 200)

    def test_pet_update(self):
        self.assertEqual(self.pet.update(data=pet), 200)

    def test_pet_find_by_status(self):
        self.assertEqual(self.pet.find_by_status(), 200)

    def test_pet_store_update(self):
        self.assertEqual(self.pet.update_store(data="{'name': 'name','status': 'available'}"), 200)

    def test_pet_zdelete(self):
        self.assertEqual(self.pet.delete(), 200)


if __name__ == "__main__":
    unittest.main()
