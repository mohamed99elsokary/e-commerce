from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

product = Blueprint("product", __name__)


@product.route("/Product/<int:product_id>", methods=["POST", "GET"])
def home(product_id):
    cur = mysql.connection.cursor()
    product_id = product_id
    if "loggedin" in session:
        loggedin = True
    else:
        loggedin = False
    # ----------------------add review
    if request.method == "POST":
        review = request.form.get("review")
        user_id = session.get("id")
        user_name = session.get("user_name")
        cur.execute(
            "INSERT INTO reviews SET user_id = %s , user_name = %s , review= %s , product_id = %s",
            (user_id, user_name, review, product_id),
        )
        mysql.connection.commit()
    # --------------------------get product data
    cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cur.fetchone()
    images = product["images"]
    tags = product["tags"]
    images = json.loads(images)
    tags = json.loads(tags)
    # ---------------------- get reviews
    cur.execute("SELECT * FROM reviews WHERE product_id = %s", (product_id,))
    reviews = cur.fetchall()
    reviews_count = len(reviews)

    return render_template(
        "product.html",
        loggedin=loggedin,
        product=product,
        images=images,
        reviews=reviews,
        reviews_count=reviews_count,
        tags=tags,
    )
