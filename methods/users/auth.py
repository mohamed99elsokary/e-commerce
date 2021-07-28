from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

auth = Blueprint("auth", __name__)


@auth.route("/auth", methods=["POST", "GET"])
def home():
    if "loggedin" in session:
        return redirect(url_for("home.main"))
    else:
        if request.method == "POST":
            inputt = request.form.get
            # --------------------------------register------------------------
            # taking input
            email = inputt("r-email")
            password = inputt("r-password")
            user_name = inputt("r-name")
            # setupt db connection
            cur = mysql.connection.cursor()
            if email and password and user_name != "":
                # check if the email is already taken
                cur.execute("SELECT password FROM users WHERE email = %s ", (email,))
                taken = cur.fetchall()
                for row in taken:
                    taken = row["password"]
                # if the email is used already the acc won't be created
                if len(taken) != 0:
                    return "this email is already taken"
                # if email isn't used already so creat the acc
                else:
                    cur.execute(
                        "INSERT INTO users SET email = %s , password = %s , user_name = %s",
                        (email, password, user_name),
                    )
                    mysql.connection.commit()
                    cur.execute("SELECT * FROM users WHERE email = %s ", (email,))
                    result = cur.fetchall()
                    if len(result) != 0:
                        for row in result:
                            id = row["id"]
                            user_name = row["user_name"]
                            role = row["role"]
                    session["loggedin"] = True
                    session["id"] = id
                    session["user_name"] = user_name
                    session["role"] = role
                    return redirect(url_for("home.main"))

            # ------------------------------------------------------------------------------login
            email = inputt("l-email")
            password = inputt("l-password")
            if email and password != "":
                cur.execute(
                    "SELECT * FROM users WHERE email = %s AND password = %s",
                    (email, password),
                )
                result = cur.fetchall()
                if len(result) != 0:
                    for row in result:
                        id = row["id"]
                        user_name = row["user_name"]
                        role = row["role"]

                        session["loggedin"] = True
                        session["id"] = id
                        session["user_name"] = user_name
                        session["role"] = role
                        return redirect(url_for("home.main"))

                else:
                    return "wrong password"

        return render_template("login.html")