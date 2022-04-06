import flask
from ...common.validate import validateExist
from firebase_admin import auth,db
from ...common.sendEmail import sendEmail

users=flask.Blueprint('users',__name__)

#Login Usuario

@users.route('/login',methods=['POST'])
def login(): 
  try:  
    data=flask.request.json
    email=data['email']
    password=data['password']
    user=auth.get_user_by_email(email) 
    if(user):
      usuario=db.reference("/usuarios").child(user.uid).get()
      print(usuario)
      if(usuario["password"]== password):
        token=str(auth.create_custom_token(user.uid,usuario)).split("'")[1]
        return flask.jsonify({"token":token})
      else:
        return flask.jsonify({"Message":"Contraseña Erronea intente nuevamente"})
    else:
      return flask.jsonify({"Message":"Usuario No esta registrado"})
  except :
    return flask.jsonify({"Message":"Datos Incorrectos"})
  # Registro Usuarios

@users.route('/registro',methods=['POST'])
def registroUsuarios():
  try:
    reference=db.reference("/usuarios")
    data=flask.request.json
    usuarios={
    "nombre":data["nombre"],
    "typeDoc":data["typeDoc"],
    "numDoc":data["numDoc"],
    "userName":data["userName"],
    "password":data["password"],
    "email":data["email"],
    "phone":data["phone"],
    "state":"1"
    }  
    if(validateExist(reference,usuarios,"numDoc")):
      return flask.jsonify({"Mensaje":"Ya existe un usuario creado con ese cedula"})
    else:
      create=auth.create_user(email=data["email"],password=data["password"])
      reference.child(create.uid).set(usuarios)
      sendEmail(data["email"],data["nombre"],1)
      return flask.jsonify({"Mensaje":"usuario Creado satisfactoriamente","UID":create.uid})
  except auth.EmailAlreadyExistsError:
    return flask.jsonify({"Mensaje":"Ya existe un usuario creado con ese correo"})
    
# Obtener usuario en especifico
@users.route('/usuarios<string:uid>')
def listaUsuariosUid(uid):
  try:
    database = db.reference("/usuarios").child(uid).get()
    return flask.jsonify(database)
  except :
    return flask.jsonify({"Mensaje":"Error trayendo el usuario"})
