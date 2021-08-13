from flask import Flask
from contactbook import Contact, ContactBook

contacts = ContactBook()

app = Flask(__name__)

@app.route("/")
def index():
    return "{0}".format(contacts.index())

