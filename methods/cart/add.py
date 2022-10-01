from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

add = Blueprint("add", __name__)


@add.route("/add/<int:product_id>", methods=["POST", "GET"])
def home(product_id):
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        loggedin = True
        user_id = session["id"]
        cur.execute(
            "SELECT quantity FROM cart WHERE user_id = %s AND closed = %s AND product_id = %s",
            (user_id, 0, product_id),
        )
        product = cur.fetchone()
        print(user_id, product_id, 0)
        if product != None:
            quantity = product["quantity"] + 1
            cur.execute(
                "UPDATE cart SET quantity = %s  WHERE user_id = %s AND product_id = %s",
                (quantity, user_id, product_id),
            )
        else:
            cur.execute(
                "INSERT INTO cart SET user_id =%s , product_id =%s , quantity = %s",
                (user_id, product_id, 1),
            )
        mysql.connection.commit()
    else:
        loggedin = False
    return redirect(url_for("auth.home"))
