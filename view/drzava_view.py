import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/drzava_view', view_func=dodavanje_drzava_view, methods=['POST'])
    app.add_url_rule('/api/drzava_view', view_func=get_all_drzava_view, methods=['GET'])
    app.add_url_rule('/api/drzava_view/<int:iddrzava>', view_func=get_drzava_view, methods=['GET'])
    app.add_url_rule('/api/drzava_view/<int:iddrzava>', view_func=izmeni_drzava_view, methods=['PUT'])
    app.add_url_rule('/api/drzava_view/<int:iddrzava>', view_func=ukloni_drzava_view, methods=['DELETE'])

def get_all_drzava_view():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava_view")
    drzava_view = cursor.fetchall()
    return flask.jsonify(drzava_view)

def get_drzava_view(iddrzava):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava_view WHERE iddrzava=%s", (iddrzava,))
    drzava_view = cursor.fetchone()
    if drzava_view is not None:
        return flask.jsonify(drzava_view)
    return "", 404

def dodavanje_drzava_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO drzava_view(drzava) VALUES (%(drzava)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_drzava_view(iddrzava):
    drzava_view = dict(flask.request.json)
    drzava_view["iddrzava"] = iddrzava
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE drzava_view SET drzava=%(drzava)s, WHERE iddrzava=%(iddrzava)s", drzava_view)
    db.commit()
    cursor.execute("SELECT * FROM drzava_view WHERE iddrzava=%s", (iddrzava, ))
    drzava_view = cursor.fetchone()
    return flask.jsonify(drzava_view)

def ukloni_drzava_view(iddrzava):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM drzava_view WHERE iddrzava=%s", (iddrzava, ))
    db.commit()
    return ""

