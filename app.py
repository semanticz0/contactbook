from flask import Flask, request, render_template, redirect
import json
import sqlite3
from contactbook import ContactDatabase, Contact

connection= sqlite3.connect('persistent.db', check_same_thread=False)
contactbook = ContactDatabase(connection)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", contacts=contactbook.index())

@app.route("/add", methods=["POST"])
def add():
    contact = Contact(request.form["name"], request.form["phone"])
    contactbook.add(contact)
    return redirect("/")

@app.route("/edit/<id_>", methods=["GET"])
def edit(id_):
    contact = contactbook.find(id_)
    return render_template("edit.html", contact=contact)
        
@app.route("/update/<id_>", methods=["POST"])
def update(id_):
    contact = Contact(request.form["name"], request.form["phone"])
    contactbook.update(id_, contact)
    return redirect("/")

@app.route("/remove/<id_>")
def remove(id_):
    contactbook.remove(id_)
    return redirect("/")
