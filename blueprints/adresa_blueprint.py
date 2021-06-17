import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
adresa_blueprint = Blueprint("adresa_blueprint", __name__)

@adresa_blueprint.route("", methods=["GET"], endpoint='get_all_adresa')
@jwt_required()
def get_all_adresa():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM adresa_view")
    adresa_view = cursor.fetchall()

    cursor.execute("SELECT * FROM drzava_view")
    drzave = cursor.fetchall()

    cursor.execute("SELECT * FROM opstina_view")
    opstine = cursor.fetchall()

    return {1: adresa_view, 2: drzave, 3: opstine}

@adresa_blueprint.route("<int:idadresa>", methods=["GET"], endpoint='get_adresa')
@jwt_required()
def get_adresa(idadresa):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM adresa_view WHERE idadresa=%s", (idadresa,))
    adresa_view = cursor.fetchone()
    if adresa_view is not None:
        return flask.jsonify(adresa_view)
    return "", 404

@adresa_blueprint.route("", methods=["POST"], endpoint='dodavanje_adresa')
@jwt_required()
def dodavanje_adresa():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO adresa(idmesto, ulica, broj) VALUES (%(idmesto)s, %(ulica)s, %(broj)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@adresa_blueprint.route("<int:idadresa>", methods=["PUT"], endpoint='izmeni_adresa')
@jwt_required()
def izmeni_adresa(idadresa):
    adresa_view = dict(flask.request.json)
    adresa_view["idadresa"] = idadresa
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE adresa SET idmesto=%(idmesto)s, ulica=%(ulica)s, broj=%(broj)s WHERE idadresa=%(idadresa)s", adresa_view)
    db.commit()
    cursor.execute("SELECT * FROM adresa_view WHERE idadresa=%s", (idadresa, ))
    adresa_view = cursor.fetchone()
    return flask.jsonify(adresa_view)

@adresa_blueprint.route("<int:idadresa>", methods=["DELETE"], endpoint='ukloni_adresa')
@jwt_required()
def ukloni_adresa(idadresa):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM adresa WHERE idadresa=%s", (idadresa, ))
    db.commit()
    return ""

@adresa_blueprint.route("pretraga", endpoint='pretraga', methods=["POST"],)
@jwt_required()
def pretraga():
    objekat = flask.request.json
    tekst = "SELECT * FROM adresa_view WHERE "
    for key, value in objekat.items():
        tekst += "{}='{}' AND ".format(key, value)

    tekst = tekst[0:-4]
    cursor = mysql.get_db().cursor()
    cursor.execute(tekst)
    adresa_view = cursor.fetchall()
    return flask.jsonify(adresa_view)

