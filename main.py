from flask import Flask
from flaskext.mysql import MySQL
from flaskext.mysql import pymysql

from view import drzava_view
from view import korisnik_view
from view import investitor_view
from view import katastarska_opstina_view
from view import mesto_view
from view import opstina_view

app = Flask(__name__, static_url_path="/")
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "geodetska_firma"

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)


drzava_view.init(app, mysql)
korisnik_view.init(app, mysql)
investitor_view.init(app, mysql)
katastarska_opstina_view.init(app, mysql)
mesto_view.init(app, mysql)
opstina_view.init(app, mysql)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route('/<path:path>')  
def send_file(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)