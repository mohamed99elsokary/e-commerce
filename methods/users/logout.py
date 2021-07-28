from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session
from status import *
import json

logout = Blueprint("logout", __name__)


@logout.route("/logout", methods=["POST", "GET"])
def home():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("first_name", None)
    return redirect(url_for("home.main"))
