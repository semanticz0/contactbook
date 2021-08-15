import sqlite3

class ContactBook:
    def __init__(self):
        self.db = DatabaseWrapper()

    def index(self):
        self.db.cur.execute(
                "SELECT contact_id, name, phone FROM contact")
        return self.db.cur.fetchall()

    def find(self, id_):
        self.db.cur.execute(
                "SELECT contact_id, name, phone FROM contact WHERE contact_id=?",
                (id_,))
        return self.db.cur.fetchone()
        
    def add(self, name, phone):
        self.db.cur.execute(
            "INSERT INTO contact (name, phone) VALUES (?, ?)", 
            (name, phone))
        self.db.con.commit()

    def remove(self, id_):
        self.db.cur.execute("DELETE FROM contact WHERE contact_id=?",
                (id_,))
        self.db.con.commit()

    def update(self, id_, name, phone):
        self.db.cur.execute(
                "UPDATE contact SET name=?, phone=? WHERE contact_id=?",
                (name, phone, id_))
        self.db.con.commit()

class DatabaseWrapper:
    def __init__(self):
        self.con = sqlite3.connect("persistent.db",
                check_same_thread=False)
        self.cur = self.con.cursor()
