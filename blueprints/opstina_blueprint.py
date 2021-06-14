import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
opstina_blueprint = Blueprint("opstina_blueprint", __name__)

@opstina_blueprint.route("", methods=["GET"], endpoint='get_all_opstina')
@jwt_required()
def get_all_opstina():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM opstina_view")
    opstina_view = cursor.fetchall()

    cursor.execute("SELECT * FROM drzava_view")
    drzave = cursor.fetchall()
    
    return {1: opstina_view, 2: drzave}

@opstina_blueprint.route("<int:idopstina>", methods=["GET"], endpoint='get_opstina')
@jwt_required()
def get_opstina(idopstina):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM opstina_view WHERE idopstina=%s", (idopstina,))
    opstina_view = cursor.fetchone()
    if opstina_view is not None:
        return flask.jsonify(opstina_view)
    return "", 404

@opstina_blueprint.route("", methods=["POST"], endpoint='dodavanje_opstina')
@jwt_required()
def dodavanje_opstina():
    db = mysql.get_db()
    cursor = db.cursor()
    print(flask.request.json)
    cursor.execute("INSERT INTO opstina(opstina, iddrzava) VALUES (%(opstina)s, %(iddrzava)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@opstina_blueprint.route("<int:idopstina>", methods=["PUT"], endpoint='izmeni_opstina')
@jwt_required()
def izmeni_opstina(idopstina):
    opstina_view = dict(flask.request.json)
    opstina_view["idopstina"] = idopstina
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE opstina SET opstina=%(opstina)s, iddrzava=%(iddrzava)s WHERE idopstina=%(idopstina)s", opstina_view)
    db.commit()
    cursor.execute("SELECT * FROM opstina_view WHERE idopstina=%s", (idopstina, ))
    opstina_view = cursor.fetchone()
    return flask.jsonify(opstina_view)

@opstina_blueprint.route("<int:idopstina>", methods=["DELETE"], endpoint='ukloni_opstina')
@jwt_required()
def ukloni_opstina(idopstina):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM opstina WHERE idopstina=%s", (idopstina, ))
    db.commit()
    return ""

