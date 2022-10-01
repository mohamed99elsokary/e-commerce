from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

blogs = Blueprint("blogs", __name__)


@blogs.route("/blogs", methods=["POST", "GET"])
def home():
    loggedin = "loggedin" in session
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blogs ")
    blogs = cur.fetchall()
    return render_template("blog.html", loggedin=loggedin, blogs=blogs)
