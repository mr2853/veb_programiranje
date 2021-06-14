import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
katastarska_opstina_blueprint = Blueprint("katastarska_opstina_blueprint", __name__)

@katastarska_opstina_blueprint.route("", methods=["GET"], endpoint='get_all_katastarska_opstina')
@jwt_required()
def get_all_katastarska_opstina():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM katastarska_opstina_view")
    katastarska_opstina_view = cursor.fetchall()

    cursor.execute("SELECT * FROM drzava_view")
    drzave = cursor.fetchall()

    cursor.execute("SELECT * FROM opstina_view")
    opstine = cursor.fetchall()

    return {1: katastarska_opstina_view, 2: drzave, 3: opstine}

@katastarska_opstina_blueprint.route("<int:idkatastarska_opstina>", methods=["GET"], endpoint='get_katastarska_opstina')
@jwt_required()
def get_katastarska_opstina(idkatastarska_opstina):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM katastarska_opstina_view WHERE idkatastarska_opstina=%s", (idkatastarska_opstina,))
    katastarska_opstina_view = cursor.fetchone()
    if katastarska_opstina_view is not None:
        return flask.jsonify(katastarska_opstina_view)
    return "", 404

@katastarska_opstina_blueprint.route("", methods=["POST"], endpoint='dodavanje_katastarska_opstina')
@jwt_required()
def dodavanje_katastarska_opstina():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO katastarska_opstina(katastarska_opstina, idopstina) VALUES (%(katastarska_opstina)s, %(idopstina)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@katastarska_opstina_blueprint.route("<int:idkatastarska_opstina>", methods=["PUT"], endpoint='izmeni_katastarska_opstina')
@jwt_required()
def izmeni_katastarska_opstina(idkatastarska_opstina):
    katastarska_opstina_view = dict(flask.request.json)
    katastarska_opstina_view["idkatastarska_opstina"] = idkatastarska_opstina
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE katastarska_opstina SET katastarska_opstina=%(katastarska_opstina)s, idopstina=%(idopstina)s WHERE idkatastarska_opstina=%(idkatastarska_opstina)s", katastarska_opstina_view)
    db.commit()
    cursor.execute("SELECT * FROM katastarska_opstina_view WHERE idkatastarska_opstina=%s", (idkatastarska_opstina, ))
    katastarska_opstina_view = cursor.fetchone()
    return flask.jsonify(katastarska_opstina_view)

@katastarska_opstina_blueprint.route("<int:idkatastarska_opstina>", methods=["DELETE"], endpoint='ukloni_katastarska_opstina')
@jwt_required()
def ukloni_katastarska_opstina(idkatastarska_opstina):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM katastarska_opstina WHERE idkatastarska_opstina=%s", (idkatastarska_opstina, ))
    db.commit()
    return ""

