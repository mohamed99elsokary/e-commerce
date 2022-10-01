from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

contact = Blueprint("contact", __name__)


@contact.route("/contact", methods=["POST", "GET"])
def main():
    loggedin = "loggedin" in session
    if request.method == "POST":
        inputt = request.form.get

        name = inputt("name")
        email = inputt("email")
        subject = inputt("subject")
        message = inputt("message")

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tickets SET name = %s , email = %s , subject = %s , message = %s",
            (name, email, subject, message),
        )
        mysql.connection.commit()
    return render_template("contact-us.html", loggedin=loggedin)
