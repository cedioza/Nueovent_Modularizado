import flask
from firebase_admin import db

home=flask.Blueprint('home',__name__)
# Home
@home.route('/home')
def anuncios():
    anuncios=db.reference("/anuncios").order_by_key().limit_to_last(6).get()
    datos=anuncios.items()
    return flask.jsonify(list(datos))

@home.route("/")
def index():
  return flask.jsonify(db.reference('/').get())

