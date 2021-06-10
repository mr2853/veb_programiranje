import flask
mysql = None

def init(app, _mysql):
    global mysql
    mysql = _mysql
    app.add_url_rule('/api/mesto_view', view_func=dodavanje_mesto_view, methods=['POST'])
    app.add_url_rule('/api/mesto_view', view_func=get_all_mesto_view, methods=['GET'])
    app.add_url_rule('/api/mesto_view/<int:idmesto>', view_func=get_mesto_view, methods=['GET'])
    app.add_url_rule('/api/mesto_view/<int:idmesto>', view_func=izmeni_mesto_view, methods=['PUT'])
    app.add_url_rule('/api/mesto_view/<int:idmesto>', view_func=ukloni_mesto_view, methods=['DELETE'])

def get_all_mesto_view():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM mesto_view")
    mesto_view = cursor.fetchall()
    return flask.jsonify(mesto_view)

def get_mesto_view(idmesto):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM mesto_view WHERE idmesto=%s", (idmesto,))
    mesto_view = cursor.fetchone()
    if mesto_view is not None:
        return flask.jsonify(mesto_view)
    return "", 404

def dodavanje_mesto_view():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO mesto_view(mesto, postanski_broj, idopstina) VALUES (%(mesto)s, %(postanski_broj)s, %(idopstina)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

def izmeni_mesto_view(idmesto):
    mesto_view = dict(flask.request.json)
    mesto_view["idmesto"] = idmesto
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE mesto_view SET mesto=%(mesto)s, postanski_broj=%(postanski_broj)s, idopstina=%(idopstina)s WHERE idmesto=%(idmesto)s", mesto_view)
    db.commit()
    cursor.execute("SELECT * FROM mesto_view WHERE idmesto=%s", (idmesto, ))
    mesto_view = cursor.fetchone()
    return flask.jsonify(mesto_view)

def ukloni_mesto_view(idmesto):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM mesto_view WHERE idmesto=%s", (idmesto, ))
    db.commit()
    return ""

