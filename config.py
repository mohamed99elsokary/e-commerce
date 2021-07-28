from imports import app

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345678"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "e-commerce"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
