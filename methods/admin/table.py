from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

table = Blueprint("table", __name__)


@table.route("/admin/<table_name>", methods=["GET", "POST"])
def home(table_name):
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        id = session.get("id")
        role = session.get("role")

        if role == "admin":
            cur.execute("SELECT * FROM " + table_name)
            mysql.connection.commit()
            results = cur.fetchall()
            keys = results[0].keys()
            return render_template(
                "admin/table.html", results=results, keys=keys, table_name=table_name
            )
        else:
            return redirect(url_for("home.main"))

    else:
        return redirect(url_for("home.main"))
