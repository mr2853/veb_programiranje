from flask_jwt_extended.utils import get_jwt
import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request

korisnik_blueprint = Blueprint("korisnik_blueprint", __name__)

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["roles"][0] == "administrator":
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Dozvoljeno samo administratorima!"), 403

        return decorator

    return wrapper

@korisnik_blueprint.route("pretraga", endpoint='pretraga', methods=["POST"],)
@jwt_required()
def pretraga():
    objekat = flask.request.json
    tekst = "SELECT * FROM korisnik_view WHERE "
    for key, value in objekat.items():
        tekst += "{}='{}' AND ".format(key, value)

    tekst = tekst[0:-4]
    cursor = mysql.get_db().cursor()
    cursor.execute(tekst)
    korisnik_view = cursor.fetchall()
    return flask.jsonify(korisnik_view)

@korisnik_blueprint.route("", methods=["GET"], endpoint='get_all_korisnik')
@jwt_required()
@admin_required()
def get_all_korisnik():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM korisnik_view")
    korisnik_view = cursor.fetchall()

    cursor.execute("SELECT * FROM tip_korisnika")
    tip_korisnika = cursor.fetchall()
    
    return {1: korisnik_view, 2: tip_korisnika}

@korisnik_blueprint.route("<int:idkorisnik>", methods=["GET"], endpoint='get_korisnik')
@jwt_required()
@admin_required()
def get_korisnik(idkorisnik):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM korisnik_view WHERE idkorisnik=%s", (idkorisnik,))
    korisnik_view = cursor.fetchone()
    if korisnik_view is not None:
        return flask.jsonify(korisnik_view)
    return "", 404

@korisnik_blueprint.route("", methods=["POST"], endpoint='dodavanje_korisnik')
@jwt_required()
@admin_required()
def dodavanje_korisnik():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO korisnik(korisnicko_ime, lozinka, idtip_korisnika) VALUES (%(korisnicko_ime)s, %(lozinka)s, %(idtip_korisnika)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@korisnik_blueprint.route("<int:idkorisnik>", methods=["PUT"], endpoint='izmeni_korisnik')
@jwt_required()
@admin_required()
def izmeni_korisnik(idkorisnik):
    korisnik_view = dict(flask.request.json)
    korisnik_view["idkorisnik"] = idkorisnik
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE korisnik SET korisnicko_ime=%(korisnicko_ime)s, lozinka=%(lozinka)s, idtip_korisnika=%(idtip_korisnika)s WHERE idkorisnik=%(idkorisnik)s", korisnik_view)
    db.commit()
    cursor.execute("SELECT * FROM korisnik_view WHERE idkorisnik=%s", (idkorisnik, ))
    korisnik_view = cursor.fetchone()
    return flask.jsonify(korisnik_view)

@korisnik_blueprint.route("<int:idkorisnik>", methods=["DELETE"], endpoint='ukloni_korisnik')
@jwt_required()
@admin_required()
def ukloni_korisnik(idkorisnik):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM korisnik WHERE idkorisnik=%s", (idkorisnik, ))
    db.commit()
    return ""

