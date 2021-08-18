from exceptions import InputError

class ContactDatabase:
   
    # :connection param must be a connection-object compliant with the DB API 2.0 protocol
    def __init__(self, connection):
        self.con = connection
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
        self.con.commit()

    def remove(self, id_):
        self.cur.execute("DELETE FROM contact WHERE contact_id=?",
                (id_,))
        self.con.commit()

    def update(self, id_, contact):
        self.cur.execute(
                "UPDATE contact SET name=?, phone=? WHERE contact_id=?",
                (contact.name, contact.phone, id_))
        self.con.commit()

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
