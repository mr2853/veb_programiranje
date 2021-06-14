import flask
from flask_jwt_extended import jwt_required
from utils.db import mysql
from flask import Blueprint
investitor_blueprint = Blueprint("investitor_blueprint", __name__)

@investitor_blueprint.route("", methods=["GET"], endpoint='get_all_investitor')
@jwt_required()
def get_all_investitor():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM investitor_view")
    investitor_view = cursor.fetchall()

    cursor.execute("SELECT * FROM drzava_view")
    drzave = cursor.fetchall()

    cursor.execute("SELECT * FROM opstina_view")
    opstine = cursor.fetchall()

    cursor.execute("SELECT * FROM mesto_view")
    mesta = cursor.fetchall()

    cursor.execute("SELECT * FROM adresa_view")
    adrese = cursor.fetchall()

    return {1: investitor_view, 2: drzave, 3: opstine, 4: mesta, 5: adrese}

@investitor_blueprint.route("<int:idinvestitor>", methods=["GET"], endpoint='get_investitor')
@jwt_required()
def get_investitor(idinvestitor):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM investitor_view WHERE idinvestitor=%s", (idinvestitor,))
    investitor_view = cursor.fetchone()
    if investitor_view is not None:
        return flask.jsonify(investitor_view)
    return "", 404

@investitor_blueprint.route("", methods=["POST"], endpoint='dodavanje_investitor')
@jwt_required()
def dodavanje_investitor():
    db = mysql.get_db()
    cursor = db.cursor()
    objekat = flask.request.json
    cursor.execute("SELECT idadresa FROM adresa_view WHERE idmesto=%(idmesto)s AND ulica=%(ulica)s AND broj=%(broj)s", objekat)
    adresa = cursor.fetchone()
    if adresa is not None:
        objekat['idadresa'] = adresa['idadresa']
    else:
        cursor.execute("INSERT INTO adresa(idmesto, ulica, broj) VALUES (%(idmesto)s, %(ulica)s, %(broj)s)", objekat)
        db.commit()
        cursor.execute("SELECT idadresa FROM adresa_view WHERE idmesto=%(idmesto)s AND ulica=%(ulica)s AND broj=%(broj)s", objekat)
        adresa = cursor.fetchone()
        objekat['idadresa'] = adresa['idadresa']

    cursor.execute("INSERT INTO investitor(ime, prezime, jmbg, broj_mobilnog, email, idadresa) VALUES (%(ime)s, %(prezime)s, %(jmbg)s, %(broj_mobilnog)s, %(email)s, %(idadresa)s)", objekat)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@investitor_blueprint.route("<int:idinvestitor>", methods=["PUT"], endpoint='izmeni_investitor')
@jwt_required()
def izmeni_investitor(idinvestitor):
    investitor_view = dict(flask.request.json)
    investitor_view["idinvestitor"] = idinvestitor
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT idadresa FROM adresa_view WHERE idmesto=%(idmesto)s AND ulica=%(ulica)s AND broj=%(broj)s", investitor_view)
    adresa = cursor.fetchone()
    if adresa is not None:
        investitor_view['idadresa'] = adresa['idadresa']
    else:
        cursor.execute("INSERT INTO adresa(idmesto, ulica, broj) VALUES (%(idmesto)s, %(ulica)s, %(broj)s)", investitor_view)
        db.commit()
        cursor.execute("SELECT idadresa FROM adresa_view WHERE idmesto=%(idmesto)s AND ulica=%(ulica)s AND broj=%(broj)s", investitor_view)
        adresa = cursor.fetchone()
        investitor_view['idadresa'] = adresa['idadresa']

    cursor.execute("UPDATE investitor SET ime=%(ime)s, prezime=%(prezime)s, jmbg=%(jmbg)s, broj_mobilnog=%(broj_mobilnog)s, email=%(email)s, idadresa=%(idadresa)s WHERE idinvestitor=%(idinvestitor)s", investitor_view)
    db.commit()
    cursor.execute("SELECT * FROM investitor_view WHERE idinvestitor=%s", (idinvestitor, ))
    investitor_view = cursor.fetchone()
    return flask.jsonify(investitor_view)

@investitor_blueprint.route("<int:idinvestitor>", methods=["DELETE"], endpoint='ukloni_investitor')
@jwt_required()
def ukloni_investitor(idinvestitor):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM investitor WHERE idinvestitor=%s", (idinvestitor, ))
    db.commit()
    return ""

