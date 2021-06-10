import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/korisnik_view', view_func=dodavanje_korisnik_view, methods=['POST'])
    app.add_url_rule('/api/korisnik_view', view_func=get_all_korisnik_view, methods=['GET'])
    app.add_url_rule('/api/korisnik_view/<int:idkorisnik>', view_func=get_korisnik_view, methods=['GET'])
    app.add_url_rule('/api/korisnik_view/<int:idkorisnik>', view_func=izmeni_korisnik_view, methods=['PUT'])
    app.add_url_rule('/api/korisnik_view/<int:idkorisnik>', view_func=ukloni_korisnik_view, methods=['DELETE'])

def get_all_korisnik_view():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM korisnik_view")
    korisnik_view = cursor.fetchall()
    return flask.jsonify(korisnik_view)

def get_korisnik_view(idkorisnik):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM korisnik_view WHERE idkorisnik=%s", (idkorisnik,))
    korisnik_view = cursor.fetchone()
    if korisnik_view is not None:
        return flask.jsonify(korisnik_view)
    return "", 404

def dodavanje_korisnik_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO korisnik(korisnicko_ime, lozinka, tip_korisnika) VALUES (%(korisnicko_ime)s, %(lozinka)s, %(tip_korisnika)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_korisnik_view(idkorisnik):
    korisnik_view = dict(flask.request.json)
    korisnik_view["idkorisnik"] = idkorisnik
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE korisnik SET korisnicko_ime=%(korisnicko_ime)s, lozinka=%(lozinka)s, tip_korisnika=%(tip_korisnika)s WHERE idkorisnik=%(idkorisnik)s", korisnik_view)
    db.commit()
    cursor.execute("SELECT * FROM korisnik_view WHERE idkorisnik=%s", (idkorisnik, ))
    korisnik_view = cursor.fetchone()
    return flask.jsonify(korisnik_view)

def ukloni_korisnik_view(idkorisnik):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM korisnik WHERE idkorisnik=%s", (idkorisnik, ))
    db.commit()
    return ""

