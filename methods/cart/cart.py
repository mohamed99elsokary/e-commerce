from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

cart = Blueprint("cart", __name__)


@cart.route("/cart", methods=["POST", "GET"])
def home():
    cur = mysql.connection.cursor()
    if "loggedin" in session:
        loggedin = True
    else:
        loggedin = False
        return redirect(url_for("auth.home"))
    # ----------------------add review------------------------
    """if request.method == "POST":
        review = request.form.get("review")
        user_id = session.get("id")
        user_name = session.get("user_name")
        cur.execute(
            "INSERT INTO reviews SET user_id = %s , user_name = %s , review= %s , product_id = %s",
            (user_id, user_name, review, product_id),
        )
        mysql.connection.commit()"""
    # --------------------------get product data -------------
    id = session.get("id")
    cur.execute("SELECT * FROM cart WHERE user_id = %s AND closed = 0", (id,))
    products = cur.fetchall()
    total = 0
    shipping = 0 if len(products) == 0 else 10
    for product in products:
        cur.execute("SELECT * FROM products WHERE id = %s", (product["product_id"],))
        data = cur.fetchone()
        product["name"] = data["name"]
        product["product_id"] = data["id"]
        product["image"] = data["image"]
        product["price"] = data["price"]

        total += product["price"] * product["quantity"]

    return render_template(
        "cart.html",
        loggedin=loggedin,
        products=products,
        shipping=shipping,
        total=total + shipping,
        id=id,
    )
