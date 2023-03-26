import unittest
from main import PhoneBook


class AddTestCase(unittest.TestCase):

    @staticmethod
    def test_len_zero():
        phone_book = PhoneBook()
        assert len(phone_book.records) == 0

    @staticmethod
    def test_add_entry():
        """The terminal will ask you to enter some values, please enter info"""
        phone_book = PhoneBook()
        phone_book.add_entry_phonebook()
        assert len(phone_book.records) == 1

    @staticmethod
    def test_del_entry():
        """The terminal will ask you to enter a name, enter ('Adi' or 'Pu')
        or ('adi' or 'pu'), end then enter 'y'"""
        phone_book = PhoneBook([
            {
                "name": "Adi",
                "surname": "Das",
                "phone_number": "555444333",
                "log_ista": "AdiGermany"
            },
            {
                "name": "Pu",
                "surname": "Ma",
                "phone_number": "555666777",
                "log_ista": "PumaGermany"
            }])
        phone_book.delete_entry_name_phonebook()
        assert len(phone_book.records) == 1
