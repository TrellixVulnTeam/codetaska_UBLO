import unittest
from test_pet import TestPet
from test_user import TestUser
from test_store import TestStore
from unittest import TestSuite


def load_tests(loader, test, pattern):
    suite = TestSuite()
    for test_class in (TestPet, TestUser, TestStore):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


unittest.main(verbosity=2)
