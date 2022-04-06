import flask
from ...common.validate import validateExist
from firebase_admin import auth,db
from ...common.sendEmail import sendEmail
import cloudinary

anounces=flask.Blueprint('anounces',__name__)

#Search  Anounce
@anounces.route('/obteneranuncio/<string:uid>',methods=['GET'])
def obtenerAnuncio(uid):

  try:
    anounce=db.reference('/anuncios').child(uid).get()
    alojamiento=db.reference('/alojamiento').child(anounce["uidAlojamiento"]).get()
    anounce["telefono"]=alojamiento["telefono"]
    anounce["email"]=alojamiento["email"]
    anounceArray=[]
    anounceArray.append(anounce)
    return flask.jsonify(anounceArray)
  except :
    return flask.jsonify({"Message":"Error obteniendo el anuncio"})
#Create Anounce

@anounces.route('/anuncio',methods=['POST'])
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

# get anounces 
@anounces.route('/misanuncios/<string:uid>')
def myAnounces(uid):
 
  try:
    anuncios=db.reference('/anuncios').get()
    myAnounce=[]
    totalAnounce=[]
    if(anuncios):
       for key, value in anuncios.items():
         if(value["uidAlojamiento"] == uid):
           myAnounce.append(key) 
           data=db.reference('/anuncios').child(key).get()
           totalAnounce.append(data)
    return flask.jsonify(list(zip(myAnounce,totalAnounce)))
  except :
    return flask.jsonify({"Message":"uid incorrecto intente nuevamente" })

@anounces.route('/anuncios')
def zone_anounces():
  anuncios=db.reference("/anuncios").get()
  data=anuncios.items()
  return flask.jsonify(list(data))
