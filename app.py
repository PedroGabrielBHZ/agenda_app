from flask import Flask, redirect, render_template, request

import db_manager

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/contacts/<id>")
def contact(id):
    contact = db_manager.get_contact(int(id))
    print(contact)
    return render_template("contact.html", contact=contact)


@app.route("/contacts/")
def contacts():
    contacts = db_manager.get_contacts()
    return render_template("contacts.html", contacts=contacts)


@app.route("/contacts/<id>", methods=["DELETE"])
def delete_contact(id):
    db_manager.delete_contact(int(id))
    contacts = db_manager.get_contacts()
    return render_template("contacts.html", contacts=contacts)


@app.route("/commitments/")
def commitments():
    commitments = db_manager.get_all_commitments()
    return render_template("commitments.html", commitments=commitments)


@app.route("/commitments/<id>", methods=["DELETE"])
def delete_commitment(id):
    db_manager.delete_commitment(int(id))
    commitments = db_manager.get_all_commitments()
    return render_template("commitments.html", commitments=commitments)


@app.route("/commitments/new", methods=["GET"])
def commitments_new_get():
    return render_template("new_commitment.html")


@app.route("/commitments/new", methods=["POST"])
def commitments_new():
    date = request.form["date"]
    description = request.form["description"]
    time = request.form["time"]
    location = request.form["location"]

    db_manager.create_commitment(description, date, location, time)
    return redirect("/commitments")


@app.route("/contacts/new", methods=["POST"])
def contacts_new():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]

    db_manager.create_contact(name, phone, email)
    return redirect("/contacts")


@app.route("/contacts/new", methods=["GET"])
def contacts_new_get():
    return render_template("new_contact.html")
