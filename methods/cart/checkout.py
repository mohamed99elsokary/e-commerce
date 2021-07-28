from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

checkout = Blueprint("checkout", __name__)


@checkout.route("/checkout", methods=["POST", "GET"])
def home():
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        loggedin = True
        user_id = session["id"]
        cur.execute("UPDATE cart SET closed = 1 WHERE user_id = %s", (user_id,))
        mysql.connection.commit()

    else:
        loggedin = False
    return redirect(url_for("auth.home"))
