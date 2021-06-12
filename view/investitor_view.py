import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/investitor_view', view_func=dodavanje_investitor_view, methods=['POST'])
    app.add_url_rule('/api/investitor_view', view_func=get_all_investitor_view, methods=['GET'])
    app.add_url_rule('/api/investitor_view/<int:idinvestitor>', view_func=get_investitor_view, methods=['GET'])
    app.add_url_rule('/api/investitor_view/<int:idinvestitor>', view_func=izmeni_investitor_view, methods=['PUT'])
    app.add_url_rule('/api/investitor_view/<int:idinvestitor>', view_func=ukloni_investitor_view, methods=['DELETE'])

def get_all_investitor_view():
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

def get_investitor_view(idinvestitor):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM investitor_view WHERE idinvestitor=%s", (idinvestitor,))
    investitor_view = cursor.fetchone()
    if investitor_view is not None:
        return flask.jsonify(investitor_view)
    return "", 404

def dodavanje_investitor_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO investitor(ime, prezime, jmbg, broj_mobilnog, email, idadresa) VALUES (%(ime)s, %(prezime)s, %(jmbg)s, %(broj_mobilnog)s, %(email)s, %(idadresa)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_investitor_view(idinvestitor):
    investitor_view = dict(flask.request.json)
    investitor_view["idinvestitor"] = idinvestitor
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE investitor SET ime=%(ime)s, prezime=%(prezime)s, jmbg=%(jmbg)s, broj_mobilnog=%(broj_mobilnog)s, email=%(email)s, idadresa=%(idadresa)s WHERE idinvestitor=%(idinvestitor)s", investitor_view)
    db.commit()
    cursor.execute("SELECT * FROM investitor_view WHERE idinvestitor=%s", (idinvestitor, ))
    investitor_view = cursor.fetchone()
    return flask.jsonify(investitor_view)

def ukloni_investitor_view(idinvestitor):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM investitor WHERE idinvestitor=%s", (idinvestitor, ))
    db.commit()
    return ""

