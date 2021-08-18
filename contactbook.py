from exceptions import InputError

class ContactDatabase:
   
    # :connection param must be a connection-object compliant with the DB API 2.0 protocol
    # ContactBook sets isolation-level to None, thereby enabling auto-commit. This may
    # create other issues when under high load, and may open you up to various vulnerabilities.
    # However, scale is not an issue here.  

    def __init__(self, connection):
        self.con = connection
        self.con.isolation_level = None
        self.cur = self.con.cursor()

    def index(self):
        self.cur.execute(
                "SELECT contact_id, name, phone FROM contact")
        return self.cur.fetchall()

    def find(self, id_):
        self.cur.execute(
                "SELECT contact_id, name, phone FROM contact WHERE contact_id=?",
                (id_,))
        return self.cur.fetchone()
        
    def add(self, contact):
        self.cur.execute(
            "INSERT INTO contact (name, phone) VALUES (?, ?)", 
            (contact.name, contact.phone))

    def remove(self, id_):
        self.cur.execute("DELETE FROM contact WHERE contact_id=?",
                (id_,))

    def update(self, id_, contact):
        self.cur.execute(
                "UPDATE contact SET name=?, phone=? WHERE contact_id=?",
                (contact.name, contact.phone, id_))

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

