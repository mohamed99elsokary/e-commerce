from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

tables = Blueprint("tables", __name__)


@tables.route("/admin", methods=["GET", "POST"])
def home():
    cur = mysql.connection.cursor()
    if "loggedin" not in session:
        return redirect(url_for("home.main"))
    id = session.get("id")
    role = session.get("role")

    if role != "admin":
        return redirect(url_for("home.main"))

    cur.execute("SHOW TABLES ")
    mysql.connection.commit()
    results = cur.fetchall()
    tables = [i["Tables_in_e-commerce"] for i in results]
    return render_template("admin/navbar.html", tables=tables)
