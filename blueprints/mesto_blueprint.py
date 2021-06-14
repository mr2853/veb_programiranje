import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
mesto_blueprint = Blueprint("mesto_blueprint", __name__)

@mesto_blueprint.route("", methods=["GET"], endpoint='get_all_mesto')
@jwt_required()
def get_all_mesto():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM mesto_view")
    mesto_view = cursor.fetchall()

    cursor.execute("SELECT * FROM drzava_view")
    drzave = cursor.fetchall()

    cursor.execute("SELECT * FROM opstina_view")
    opstine = cursor.fetchall()

    return {1: mesto_view, 2: drzave, 3: opstine}

@mesto_blueprint.route("<int:idmesto>", methods=["GET"], endpoint='get_mesto')
@jwt_required()
def get_mesto(idmesto):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM mesto_view WHERE idmesto=%s", (idmesto,))
    mesto_view = cursor.fetchone()
    if mesto_view is not None:
        return flask.jsonify(mesto_view)
    return "", 404

@mesto_blueprint.route("", methods=["POST"], endpoint='dodavanje_mesto')
@jwt_required()
def dodavanje_mesto():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO mesto(mesto, postanski_broj, idopstina) VALUES (%(mesto)s, %(postanski_broj)s, %(idopstina)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@mesto_blueprint.route("<int:idmesto>", methods=["PUT"], endpoint='izmeni_mesto')
@jwt_required()
def izmeni_mesto(idmesto):
    mesto_view = dict(flask.request.json)
    mesto_view["idmesto"] = idmesto
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE mesto SET mesto=%(mesto)s, postanski_broj=%(postanski_broj)s, idopstina=%(idopstina)s WHERE idmesto=%(idmesto)s", mesto_view)
    db.commit()
    cursor.execute("SELECT * FROM mesto_view WHERE idmesto=%s", (idmesto, ))
    mesto_view = cursor.fetchone()
    return flask.jsonify(mesto_view)

@mesto_blueprint.route("<int:idmesto>", methods=["DELETE"], endpoint='ukloni_mesto')
@jwt_required()
def ukloni_mesto(idmesto):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM mesto WHERE idmesto=%s", (idmesto, ))
    db.commit()
    return ""

