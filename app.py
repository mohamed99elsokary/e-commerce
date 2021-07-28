from config import app
from flask import render_template

app.config["SECRET_KEY"] = "dk;vnjfvdfblkcvjn klasdanfivsndsj"
# ----------------home------------------
from methods.home.home import home
from methods.home.contact import contact

# ----------------cart------------------
from methods.cart.cart import cart
from methods.cart.remove import remove
from methods.cart.checkout import checkout
from methods.cart.add import add

# ----------------blogs------------------
from methods.blogs.blogs import blogs
from methods.blogs.blog import blog

# ----------------products------------------
from methods.products.Products import Products
from methods.products.product import product

# ----------------users------------------
from methods.users.auth import auth
from methods.users.logout import logout
from methods.users.edit import edit
from methods.users.delete import delete
from methods.users.reset_password import reset_password

# --------------------------------404------------------------
from methods.error import error

# -----------------------------admin---------------
from methods.admin.tables import tables
from methods.admin.table import table
from methods.admin.admin_delete import admin_delete

# ----------------home---------------
app.register_blueprint(home)
app.register_blueprint(contact)
# ----------------blogs------------------
app.register_blueprint(blogs)
app.register_blueprint(blog)
# ----------------products------------------
app.register_blueprint(Products)
app.register_blueprint(product)
# ----------------users------------------
app.register_blueprint(auth)
app.register_blueprint(logout)
app.register_blueprint(edit)
app.register_blueprint(delete)
app.register_blueprint(reset_password)
# --------------------------------404------------------------
app.register_blueprint(error)
# -----------------------------admin---------------

app.register_blueprint(tables)
app.register_blueprint(table)
app.register_blueprint(admin_delete)
# --------------------------------cart------------------------
app.register_blueprint(cart)
app.register_blueprint(checkout)
app.register_blueprint(remove)
app.register_blueprint(add)

# ----------------items---------------
"""from items.add import add
app.register_blueprint(add)"""
"""from items.edit import edit
app.register_blueprint(edit)"""
"""from items.delete import delete
app.register_blueprint(delete)"""


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="192.168.1.2", port=80, debug=True)
