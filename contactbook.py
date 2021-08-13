import sqlite3

class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

        self.con = sqlite3.connect('persistent.db')
        self.cur = self.con.cursor()

        self.cur.execute("INSERT INTO contact (name, phone) VALUES ('{0}','{1}')".format(self.name, self.phone))
        self.con.commit()

    def __str__(self):
        return self.name

class ContactBook:
    def __init__(self):
        self.con = sqlite3.connect('persistent.db')
        self.cur = self.con.cursor()

    def index(self):
        self.cur.execute('SELECT * FROM contact')
        return self.cur.fetchall()

    def add(self, name, phone):
        contact = Contact(name, phone)
