import flask
from flask_jwt_extended import create_access_token
from utils.db import mysql
from flask import Blueprint
login_blueprint = Blueprint("login_blueprint", __name__)

@login_blueprint.route("", methods=["POST"], endpoint='pretraga_korisnika')
def pretraga_korisnika():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM korisnik_view WHERE korisnicko_ime=%(korisnicko_ime)s AND lozinka=%(lozinka)s", flask.request.json)
    korisnik = cursor.fetchone()
    if korisnik is not None:
        access_token = create_access_token(identity=korisnik["korisnicko_ime"], additional_claims={"roles": [korisnik["tip_korisnika"]]})
        return flask.jsonify(access_token, korisnik['tip_korisnika']), 200
    else:
        return "", 403

