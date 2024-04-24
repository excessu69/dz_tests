import unittest
from unittest import TestCase
from main import get_doc_owner_name, get_all_doc_owners_names, delete_doc

class TestSecretaryProgram(TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("11-2"), "Геннадий Покемонов")

    def test_get_all_doc_owners_names(self):
        # Учитываем, что 'Василий Гупкин' удален.
        expected = {'Аристарх Павлов', 'Геннадий Покемонов'}
        actual = get_all_doc_owners_names()
        self.assertEqual(expected, actual)

    def test_delete_doc(self):
        doc_number, deleted = delete_doc("2207 876234")
        self.assertEqual((doc_number, deleted), ("2207 876234", True))

if __name__ == '__main__':
    unittest.main()




