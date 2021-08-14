import sqlite3


def commit(func):
    def wrapper(*args, **kwargs):
        db = DatabaseWrapper()
        func(*args, **kwargs)
        db.con.commit()

    return wrapper


class ContactBook:
    def __init__(self):
        self.db = DatabaseWrapper()

    def index(self):
        self.db.cur.execute(
                "SELECT contact_id, name, phone FROM contact")
        return self.db.cur.fetchall()

    @commit
    def add(self, name, phone):
        self.db.cur.execute(
            "INSERT INTO contact (name, phone) VALUES (?, ?)", 
            (name, phone))

    @commit
    def remove(self, id_):
        self.db.cur.execute("DELETE FROM contact WHERE contact_id=?",
                (id_))


class DatabaseWrapper:
    def __init__(self):
        self.con = sqlite3.connect("persistent.db",
                check_same_thread=False)
        self.cur = self.con.cursor()
