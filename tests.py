import unittest
from contact import Contact

class TestContact(unittest.TestCase):

    def setUp(self):
        self.john = Contact("John", "9846774489")

    def tearDown(self):
        self.john.cur.execute("DELETE FROM contact WHERE phone='{0}'".format(self.john.phone))
        self.john.con.commit()
        self.john.con.close()

    def test_change_name(self):
        self.john.change_name("Ricciardo")
        self.assertEqual(self.john.name, "Ricciardo")

    def test_change_phone(self):
        self.john.change_phone("8089673202")
        self.assertEqual(self.john.phone, "8089673202")


if __name__ == "__main__":
    unittest.main()
