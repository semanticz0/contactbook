import unittest
from contactbook import ContactBook

class TestContactBook(unittest.TestCase):
    def setUp(self):
        self.contacts = ContactBook()

    def test_cannot_add_text_as_phone_number(self):
        pass


if __name__ == "__main__":
    unittest.main()
