import flask
from ...common.validate import validateExist
from firebase_admin import auth,db
from ...common.sendEmail import sendEmail
import cloudinary

anounce=flask.Blueprint('anounce',__name__)

#Buscar Anuncion
@anounce.route('/obteneranuncio/<string:uid>',methods=['GET'])
def obtenerAnuncio(uid):
  anuncio=db.reference('/anuncios').child(uid).get()
  alojamiento=db.reference('/alojamiento').child(anuncio["uidAlojamiento"]).get()

  anuncio["telefono"]=alojamiento["telefono"]
  anuncio["email"]=alojamiento["email"]
  anuncioP=[]
  anuncioP.append(anuncio)
   
  return flask.jsonify(anuncioP)

#Crear Anuncio

@anounce.route('/anuncio',methods=['POST'])
def registroAnuncios():
  try:
    reference=db.reference("/anuncios")
    data=flask.request.form
    imagen=flask.request.files 
    anuncios={
    "nomAnounce":data["nomAnounce"],
    "description":data["description"],
    "numCapacity":data["numCapacity"],
    "location":data["location"],
    "available":"available",
    "uidAlojamiento":data["uid"]
    }
    for i in range(1,len(imagen)+1):
      if(imagen.get(f"file{i}")):
        url=cloudinary.uploader.upload(imagen.get(f"file{i}"))
        anuncios[f"picture{i}"]= url["url"]
    reference.push(anuncios)

    return flask.jsonify({"Mensaje":"Anuncio creado"})
  except Exception as  e:
    reference=db.reference("/error").push(e)
    return flask.jsonify({"Mensaje":"Error creando anuncio"})

@anounce.route('/misanuncios/<string:uid>')
def misAnuncios(uid):
  anuncios=db.reference('/anuncios').get()
  try:
    misAnuncios=[]
    anuncioTotal=[]
    if(anuncios):
       for key, value in anuncios.items():
         if(value["uidAlojamiento"] == uid):
           misAnuncios.append(key) 
           data=db.reference('/anuncios').child(key).get()
           anuncioTotal.append(data)
    return flask.jsonify(list(zip(misAnuncios,anuncioTotal)))
  except :
    return flask.jsonify({"Message":"uid incorrecto intente nuevamente" })

@anounce.route('/anuncios')
def zona_anuncios():
  anuncios=db.reference("/anuncios").get()
  datos=anuncios.items()
  return flask.jsonify(list(datos))