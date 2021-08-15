import unittest
from contactbook import ContactBook

class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.contacts = ContactBook()

    def test_can_find_contact_by_phone(self):
        self.assertEqual(
                self.contacts.search(phone="1234567890"),
                [("TestUser", "1234567890")])

    def test_cannot_find_nonexistent_contact_by_phone(self):
        self.assertEqual(
                self.contacts.search(phone="194218957912751"),
                [])

    def test_cannot_add_text_as_phone_number(self):
        pass


if __name__ == "__main__":
    unittest.main()
