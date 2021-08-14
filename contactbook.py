import sqlite3

class ContactBook:
    def __init__(self):
        self.con = sqlite3.connect('persistent.db', check_same_thread=False)
        self.cur = self.con.cursor()

    def index(self):
        self.cur.execute('SELECT contact_id, name, phone FROM contact')
        return self.cur.fetchall()

    def add(self, name, phone):
        self.cur.execute("INSERT INTO contact (name, phone) VALUES (?, ?)", (name, phone))
        self.con.commit()

    def remove(self, id_):
        self.cur.execute('DELETE FROM contact WHERE contact_id=?',(id_))
        self.con.commit()

