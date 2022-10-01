from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

Products = Blueprint("Products", __name__)


@Products.route("/Products", methods=["POST", "GET"])
def main():
    loggedin = "loggedin" in session
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products ")
    products = cur.fetchall()
    brands = []
    categorys = []
    for product in products:
        brand = product["brand"]
        brands.append(brand)
        tags = product["tags"]
        tags = json.loads(tags)

        categorys.extend(iter(tags))
    categorys = set(categorys)
    brands = set(brands)

    return render_template(
        "Products.html",
        loggedin=loggedin,
        products=products,
        brands=brands,
        categorys=categorys,
    )
