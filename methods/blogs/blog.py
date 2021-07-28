from imports import app, mysql
from flask import Blueprint, request, render_template, redirect, url_for, session

from status import *
import json

blog = Blueprint("blog", __name__)


@blog.route("/blog/<int:blog_id>", methods=["POST", "GET"])
def home(blog_id):
    cur = mysql.connection.cursor()
    blog_id = blog_id
    if "loggedin" in session:
        loggedin = True
    else:
        loggedin = False
    if request.method == "POST":
        comment = request.form.get("comment")
        user_id = session.get("id")
        user_name = session.get("user_name")
        cur.execute(
            "INSERT INTO comments SET user_id = %s , user_name = %s , comment= %s , blog_id = %s",
            (user_id, user_name, comment, blog_id),
        )
        mysql.connection.commit()
    cur.execute("SELECT * FROM blogs WHERE id = %s", (blog_id,))
    blog = cur.fetchone()
    tags = blog["tags"]
    tags = json.loads(tags)
    cur.execute("SELECT * FROM comments WHERE blog_id = %s", (blog_id,))
    comments = cur.fetchall()
    comments_count = len(comments)
    return render_template(
        "blog-single.html",
        loggedin=loggedin,
        blog=blog,
        tags=tags,
        comments=comments,
        comments_count=comments_count,
    )
