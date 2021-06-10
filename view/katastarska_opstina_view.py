import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/katastarska_opstina_view', view_func=dodavanje_katastarska_opstina_view, methods=['POST'])
    app.add_url_rule('/api/katastarska_opstina_view', view_func=get_all_katastarska_opstina_view, methods=['GET'])
    app.add_url_rule('/api/katastarska_opstina_view/<int:idkatastarska_opstina>', view_func=get_katastarska_opstina_view, methods=['GET'])
    app.add_url_rule('/api/katastarska_opstina_view/<int:idkatastarska_opstina>', view_func=izmeni_katastarska_opstina_view, methods=['PUT'])
    app.add_url_rule('/api/katastarska_opstina_view/<int:idkatastarska_opstina>', view_func=ukloni_katastarska_opstina_view, methods=['DELETE'])

def get_all_katastarska_opstina_view():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM katastarska_opstina_view")
    katastarska_opstina_view = cursor.fetchall()
    return flask.jsonify(katastarska_opstina_view)

def get_katastarska_opstina_view(idkatastarska_opstina):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM katastarska_opstina_view WHERE idkatastarska_opstina=%s", (idkatastarska_opstina,))
    katastarska_opstina_view = cursor.fetchone()
    if katastarska_opstina_view is not None:
        return flask.jsonify(katastarska_opstina_view)
    return "", 404

def dodavanje_katastarska_opstina_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO katastarska_opstina_view(katastarska_opstina, idopstina) VALUES (%(katastarska_opstina)s, %(idopstina)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_katastarska_opstina_view(idkatastarska_opstina):
    katastarska_opstina_view = dict(flask.request.json)
    katastarska_opstina_view["idkatastarska_opstina"] = idkatastarska_opstina
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE katastarska_opstina_view SET katastarska_opstina=%(katastarska_opstina)s, idopstina=%(idopstina)s WHERE idkatastarska_opstina=%(idkatastarska_opstina)s", katastarska_opstina_view)
    db.commit()
    cursor.execute("SELECT * FROM katastarska_opstina_view WHERE idkatastarska_opstina=%s", (idkatastarska_opstina, ))
    katastarska_opstina_view = cursor.fetchone()
    return flask.jsonify(katastarska_opstina_view)

def ukloni_katastarska_opstina_view(idkatastarska_opstina):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM katastarska_opstina_view WHERE idkatastarska_opstina=%s", (idkatastarska_opstina, ))
    db.commit()
    return ""

