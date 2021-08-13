import sqlite3

class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

        self.con = sqlite3.connect('persistent.db')
        self.cur = self.con.cursor()

    def __str__(self):
        return self.name

    def create_user(self):
    
        self.cur.execute("INSERT INTO contact (name, phone) VALUES ('{0}','{1}')".format(self.name, self.phone))
        self.con.commit()

    def change_name(self, new_name):
        self.name = new_name

    def change_phone(self, new_phone):
        self.phone = new_phone

    def get_id(self):
        self.cur.execute('SELECT contact_id FROM contact WHERE phone="{0}"'.format(self.phone))
        self.con.commit()

class ContactBook:
    def __init__(self):
        self.con = sqlite3.connect('persistent.db')
        self.cur = self.con.cursor()

    def index(self):
        self.cur.execute('SELECT * FROM contact')
        return self.cur.fetchall()

