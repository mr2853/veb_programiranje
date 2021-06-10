import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/opstina_view', view_func=dodavanje_opstina_view, methods=['POST'])
    app.add_url_rule('/api/opstina_view', view_func=get_all_opstina_view, methods=['GET'])
    app.add_url_rule('/api/opstina_view_forma', view_func=get_forma, methods=['GET'])
    app.add_url_rule('/api/opstina_view/<int:idopstina>', view_func=get_opstina_view, methods=['GET'])
    app.add_url_rule('/api/opstina_view/<int:idopstina>', view_func=izmeni_opstina_view, methods=['PUT'])
    app.add_url_rule('/api/opstina_view/<int:idopstina>', view_func=ukloni_opstina_view, methods=['DELETE'])
    app.add_url_rule('/api/opstina_view_forma', view_func=ukloni_opstina_view)


def get_forma():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava")
    opstina_view = cursor.fetchall()
    obj = flask.jsonify(opstina_view)
    obj['zamena'] = 'iddrzava'
    return obj

def get_all_opstina_view():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM opstina_view")
    opstina_view = cursor.fetchall()
    return flask.jsonify(opstina_view)

def get_opstina_view(idopstina):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM opstina_view WHERE idopstina=%s", (idopstina,))
    opstina_view = cursor.fetchone()
    if opstina_view is not None:
        return flask.jsonify(opstina_view)
    return "", 404

def dodavanje_opstina_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO opstina_view(opstina, iddrzava) VALUES (%(opstina)s, %(iddrzava)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_opstina_view(idopstina):
    opstina_view = dict(flask.request.json)
    opstina_view["idopstina"] = idopstina
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE opstina_view SET opstina=%(opstina)s, iddrzava=%(iddrzava)s WHERE idopstina=%(idopstina)s", opstina_view)
    db.commit()
    cursor.execute("SELECT * FROM opstina_view WHERE idopstina=%s", (idopstina, ))
    opstina_view = cursor.fetchone()
    return flask.jsonify(opstina_view)

def ukloni_opstina_view(idopstina):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM opstina_view WHERE idopstina=%s", (idopstina, ))
    db.commit()
    return ""

