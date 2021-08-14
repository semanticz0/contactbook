from flask import Flask, request, render_template, redirect
import json
from contactbook import ContactBook

contactbook = ContactBook()

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        contactbook.add(request.form['name'], request.form['phone'])
        return render_template('index.html', contacts=contactbook.index())
    return render_template('index.html', contacts=contactbook.index()) 

@app.route("/delete/<id_>")
def delete(id_):
    contactbook.remove(id_)
    return redirect("/")

