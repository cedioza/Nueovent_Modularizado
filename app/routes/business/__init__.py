
import flask
from ...common.validate import validateExist
from firebase_admin import auth,db
from ...common.sendEmail import sendEmail


#Alojamiento datos con uid dado

business=flask.Blueprint("business",__name__)


@business.route('/registrarAlojamiento/<string:uid>',  methods=['POST'])
def registrarAlojamiento(uid):
  try:
    reference=db.reference("/alojamientos").child(uid)
    data=flask.request.json
    alojamiento={
    "nombrealojamiento":data["nombrealojamiento"],
    "nit":data["nit"],
    "email":data["email"],
    "telefono":data["telefono"],
    "responsable":data["responsable"],
    "categoria":data["categoria"],
    "descripcion":data["descripcion"],
    "ciudad":data["ciudad"],
    "direccion":data["direccion"],
    "proveedor":data["proveedor"]
    }
    if(validateExist(reference,alojamiento,"nit")):
      return flask.jsonify({"Mensaje":"Ya existe un alojamiento  creado con ese nit"})
    else:
      reference.set(alojamiento)
      db.reference('/usuarios').child(uid).update({"state":"2"})
      print("usuario cambio de estado ")
      return flask.jsonify({"Mensaje":"Alojamiento  Creado satisfactoriamente","UID":uid})
  except :
    return flask.jsonify({"Mensaje":"No se pudo crear el alojamiento"})        

