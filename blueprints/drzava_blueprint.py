import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
drzava_blueprint = Blueprint("drzava_blueprint", __name__)

@drzava_blueprint.route("", endpoint='get_all_drzava')
@jwt_required()
def get_all_drzava():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava_view")
    drzava_view = cursor.fetchall()
    return flask.jsonify(drzava_view)

@drzava_blueprint.route("pretraga", endpoint='pretraga', methods=["POST"],)
@jwt_required()
def pretraga():
    objekat = flask.request.json
    tekst = "SELECT * FROM drzava_view WHERE "
    for key, value in objekat.items():
        tekst += "{}='{}' AND ".format(key, value)

    tekst = tekst[0:-4]
    cursor = mysql.get_db().cursor()
    cursor.execute(tekst)
    drzava_view = cursor.fetchall()
    return flask.jsonify(drzava_view)

@drzava_blueprint.route("<int:iddrzava>", endpoint='get_drzava')
@jwt_required()
def get_drzava(iddrzava):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava_view WHERE iddrzava=%s", (iddrzava,))
    drzava_view = cursor.fetchone()
    if drzava_view is not None:
        return flask.jsonify(drzava_view)
    return "", 404

@drzava_blueprint.route("", methods=["POST"], endpoint='dodavanje_drzava')
@jwt_required()
def dodavanje_drzava():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO drzava(drzava) VALUES (%(drzava)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@drzava_blueprint.route("<int:iddrzava>", methods=["PUT"], endpoint='izmeni_drzava')
@jwt_required()
def izmeni_drzava(iddrzava):
    drzava_view = dict(flask.request.json)
    drzava_view["iddrzava"] = iddrzava
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE drzava SET drzava=%(drzava)s, WHERE iddrzava=%(iddrzava)s", drzava_view)
    db.commit()
    cursor.execute("SELECT * FROM drzava_view WHERE iddrzava=%s", (iddrzava, ))
    drzava_view = cursor.fetchone()
    return flask.jsonify(drzava_view)

@drzava_blueprint.route("<int:iddrzava>", methods=["DELETE"], endpoint='ukloni_drzava')
@jwt_required()
def ukloni_drzava(iddrzava):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM drzava WHERE iddrzava=%s", (iddrzava, ))
    db.commit()
    return ""

