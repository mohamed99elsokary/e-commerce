from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

home = Blueprint("home", __name__)


@home.route("/", methods=["POST", "GET"])
def main():
    if "loggedin" in session:
        loggedin = True
    else:
        loggedin = False
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products ORDER BY id DESC LIMIT 9 ")
    products = cur.fetchall()
    return render_template("index.html", loggedin=loggedin, products=products)
