import sqlite3
import pytest 

from exceptions import ContactNotFoundError
from contactbook import ContactDatabase, Contact

@pytest.fixture(autouse=True)
def setup():
    global contacts 
    connection = sqlite3.connect('test.db', check_same_thread=False)
    contacts = ContactDatabase(connection)

    contacts.cur.execute("CREATE TABLE contact (contact_id INTEGER PRIMARY KEY, name text, phone text)")
    contacts.cur.execute("INSERT INTO contact (name, phone) VALUES ('Nihal Sahu', '8089673202')")
    contacts.cur.execute("INSERT INTO contact (name, phone) VALUES ('Abdul Azis', '9846774889')")
    contacts.cur.execute("INSERT INTO contact (name, phone) VALUES ('Neelima Azis', '9961935299')")
    yield
    contacts.cur.execute("DROP TABLE contact")

class TestContactDatabase():
    def test_initialize_sets_isolation_level(self):
        assert contacts.con.isolation_level == None

    def test_initialize_produces_cursor(self):
        assert hasattr(contacts, 'cur') == True

    def test_index(self):
        index = contacts.index() 
        assert len(index) == 3
    
    def test_index_returns_list(self):
        index = contacts.index()
        assert isinstance(index, list)

    def test_index_returns_list_of_tuples(self):
        index = contacts.index()
        for row in index:
            assert isinstance(row, tuple)

    def test_find(self):
        results = contacts.find(1)
        assert results

    def test_find_accepts_string(self):
        results = contacts.find("1")
        assert results[1] == "Nihal Sahu"
    
    def test_add(self):
       contact = Contact('Lorelai', '9923') 
       contacts.add(contact)
       assert len(contacts.index()) == 4

    def test_remove(self):
        contacts.remove(1)
        assert contacts.find(1) is None 

    def test_remove_non_existent_id(self):
            contacts.remove(8)
            
