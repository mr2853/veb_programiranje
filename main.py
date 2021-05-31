import flask
from flask import Flask
from flaskext.mysql import MySQL
from flaskext.mysql import pymysql

app = Flask(__name__, static_url_path="/")
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "geodetska_firma"

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/api/drzava")
def get_all_drzave():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava")
    drzave = cursor.fetchall()
    return flask.jsonify(drzave)

@app.route("/api/drzava/<int:iddrzava>")
def get_drzava(iddrzava):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM drzava WHERE iddrzava=%s", (iddrzava,))
    drzava = cursor.fetchone()
    if drzava is not None:
        return flask.jsonify(drzava)
    
    return "", 404

@app.route("/api/drzava", methods=["POST"])
def dodavanje_drzava():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO drzava(iddrzava, drzava) VALUES(%(iddrzava)s, %(drzava)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@app.route("/api/drzava/<int:iddrzava>", methods=["PUT"])
def izmeni_drzava(iddrzava):
    drzava = dict(flask.request.json)
    drzava["iddrzava"] = iddrzava
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE drzava SET iddrzava=%(iddrzava)s, drzava=%(drzava)s WHERE iddrzava=%(iddrzava)s", drzava)
    db.commit()
    cursor.execute("SELECT * FROM drzava WHERE iddrzava=%s", (iddrzava, ))
    drzava = cursor.fetchone()
    return flask.jsonify(drzava)

@app.route("/api/drzava/<int:iddrzava>", methods=["DELETE"])
def ukloni_drzava(iddrzava):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM drzava WHERE iddrzava=%s", (iddrzava, ))
    db.commit()
    return ""


# Proizvodi
# @app.route("/api/proizvodi")
# def get_all_proizvodi():
#     cursor = mysql.get_db().cursor()
#     cursor.execute("SELECT * FROM proizvod")
#     proizvodi = cursor.fetchall()
#     for p in proizvodi:
#         p["cena"] = float(p["cena"])
#     return flask.jsonify(proizvodi)

# @app.route("/api/proizvodi/<int:proizvod_id>")
# def get_proizvod(proizvod_id):
#     cursor = mysql.get_db().cursor()
#     cursor.execute("SELECT * FROM proizvod WHERE id=%s", (proizvod_id,))
#     proizvod = cursor.fetchone()
#     if proizvod is not None:
#         proizvod["cena"] = float(proizvod["cena"])
#         return flask.jsonify(proizvod)
    
#     return "", 404

# @app.route("/api/proizvodi", methods=["POST"])
# def dodavanje_proizvoda():
#     db = mysql.get_db()
#     cursor = db.cursor()
#     cursor.execute("INSERT INTO proizvod(naziv, opis, cena, dostupno) VALUES(%(naziv)s, %(opis)s, %(cena)s, %(dostupno)s)", flask.request.json)
#     db.commit()
#     return flask.jsonify(flask.request.json), 201

# @app.route("/api/proizvodi/<int:proizvod_id>", methods=["PUT"])
# def izmeni_proizvod(proizvod_id):
#     proizvod = dict(flask.request.json)
#     proizvod["proizvod_id"] = proizvod_id
#     db = mysql.get_db()
#     cursor = db.cursor()
#     cursor.execute("UPDATE proizvod SET naziv=%(naziv)s, opis=%(opis)s, cena=%(cena)s, dostupno=%(dostupno)s WHERE id=%(proizvod_id)s", proizvod)
#     db.commit()
#     cursor.execute("SELECT * FROM proizvod WHERE id=%s", (proizvod_id,))
#     proizvod = cursor.fetchone()
#     proizvod["cena"] = float(proizvod["cena"])
#     return flask.jsonify(proizvod)

# @app.route("/api/proizvodi/<int:proizvod_id>", methods=["DELETE"])
# def ukloni_proizvod(proizvod_id):
#     db = mysql.get_db()
#     cursor = db.cursor()
#     cursor.execute("DELETE FROM proizvod WHERE id=%s", (proizvod_id, ))
#     db.commit()
#     return ""

if __name__ == "__main__":
    app.run(debug=True)