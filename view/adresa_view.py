import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/adresa_view', view_func=dodavanje_adresa_view, methods=['POST'])
    app.add_url_rule('/api/adresa_view', view_func=get_all_adresa_view, methods=['GET'])
    app.add_url_rule('/api/adresa_view/<int:idadresa>', view_func=get_adresa_view, methods=['GET'])
    app.add_url_rule('/api/adresa_view/<int:idadresa>', view_func=izmeni_adresa_view, methods=['PUT'])
    app.add_url_rule('/api/adresa_view/<int:idadresa>', view_func=ukloni_adresa_view, methods=['DELETE'])

def get_all_adresa_view():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM adresa_view")
    adresa_view = cursor.fetchall()
    return flask.jsonify(adresa_view)

def get_adresa_view(idadresa):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM adresa_view WHERE idadresa=%s", (idadresa,))
    adresa_view = cursor.fetchone()
    if adresa_view is not None:
        return flask.jsonify(adresa_view)
    return "", 404

def dodavanje_adresa_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO adresa_view(idmesto, ulica, broj) VALUES (%(idmesto)s, %(ulica)s, %(broj)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_adresa_view(idadresa):
    adresa_view = dict(flask.request.json)
    adresa_view["idadresa"] = idadresa
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE adresa_view SET idmesto=%(idmesto)s, ulica=%(ulica)s, broj=%(broj)s WHERE idadresa=%(idadresa)s", adresa_view)
    db.commit()
    cursor.execute("SELECT * FROM adresa_view WHERE idadresa=%s", (idadresa, ))
    adresa_view = cursor.fetchone()
    return flask.jsonify(adresa_view)

def ukloni_adresa_view(idadresa):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM adresa_view WHERE idadresa=%s", (idadresa, ))
    db.commit()
    return ""

