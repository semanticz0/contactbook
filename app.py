from flask import Flask, request, render_template, redirect
import json
from contactbook import ContactBook

contactbook = ContactBook()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", contacts=contactbook.index())

@app.route("/add", methods=["POST"])
def add():
    contactbook.add(request.form["name"], request.form["phone"])
    return redirect("/")

@app.route("/edit/<id_>", methods=["GET"])
def edit(id_):
    contact = contactbook.find(id_)
    return render_template("edit.html", contact=contact)
        
@app.route("/update/<id_>", methods=["POST"])
def update(id_):
    contactbook.update(id_, request.form["name"], request.form["phone"])
    return redirect("/")

@app.route("/remove/<id_>")
def remove(id_):
    contactbook.remove(id_)
    return redirect("/")
