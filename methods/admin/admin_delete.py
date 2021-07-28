from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

admin_delete = Blueprint("admin_delete", __name__)


@admin_delete.route("/admin/delete/<table_name>/<int:id>", methods=["GET", "POST"])
def home(table_name, id):
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        id = session.get("id")
        role = session.get("role")

        if role == "admin":
            cur.execute(f"DELETE FROM {table_name} WHERE id = {id}")
            mysql.connection.commit()
            return redirect(f"/admin/{table_name}")
        else:
            return redirect(url_for("home.main"))

    else:
        return redirect(url_for("home.main"))
