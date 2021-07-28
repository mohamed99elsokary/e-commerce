from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

tables = Blueprint("tables", __name__)


@tables.route("/admin", methods=["GET", "POST"])
def home():
    tables = []
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        id = session.get("id")
        role = session.get("role")

        if role == "admin":
            cur.execute("SHOW TABLES ")
            mysql.connection.commit()
            results = cur.fetchall()
            for i in results:
                table = i["Tables_in_e-commerce"]
                tables.append(table)

            return render_template("admin/navbar.html", tables=tables)
        else:
            return redirect(url_for("home.main"))

    else:
        return redirect(url_for("home.main"))
