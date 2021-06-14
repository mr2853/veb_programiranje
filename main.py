from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_jwt_extended.utils import get_jwt
from flaskext.mysql import MySQL
from flaskext.mysql import pymysql

from blueprints.drzava_blueprint import drzava_blueprint
from blueprints.adresa_blueprint import adresa_blueprint
from blueprints.korisnik_blueprint import korisnik_blueprint
from blueprints.investitor_blueprint import investitor_blueprint
from blueprints.katastarska_opstina_blueprint import katastarska_opstina_blueprint
from blueprints.mesto_blueprint import mesto_blueprint
from blueprints.opstina_blueprint import opstina_blueprint
from blueprints.login_blueprint import login_blueprint

from utils.db import mysql

app = Flask(__name__, static_url_path="/")
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "geodetska_firma"
app.config["JWT_SECRET_KEY"] = "txYA.EC-fh5XT+?mM4t6"

app.register_blueprint(adresa_blueprint, url_prefix="/api/adresa")
app.register_blueprint(drzava_blueprint, url_prefix="/api/drzava")
app.register_blueprint(login_blueprint, url_prefix="/api/login")
app.register_blueprint(korisnik_blueprint, url_prefix="/api/korisnik")
app.register_blueprint(investitor_blueprint, url_prefix="/api/investitor")
app.register_blueprint(katastarska_opstina_blueprint, url_prefix="/api/katastarska_opstina")
app.register_blueprint(mesto_blueprint, url_prefix="/api/mesto")
app.register_blueprint(opstina_blueprint, url_prefix="/api/opstina")

mysql.init_app(app)
jwt = JWTManager(app)



@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route('/<path:path>')  
def send_file(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)