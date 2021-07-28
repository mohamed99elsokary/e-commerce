from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

remove = Blueprint("remove", __name__)


@remove.route("/remove/<int:id>", methods=["POST", "GET"])
def home(id):
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        loggedin = True
        user_id = session["id"]
        cur.execute("DELETE FROM cart WHERE id = %s AND user_id = %s", (id, user_id))
        mysql.connection.commit()
        return redirect(url_for("cart.home"))

    else:
        loggedin = False
        return redirect(url_for("auth.home"))
