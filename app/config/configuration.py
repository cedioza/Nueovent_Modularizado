import cloudinary
from decouple import config
import requests
import firebase_admin
from firebase_admin import credentials
from flask_cors import CORS



def inicialize(app):

  # Inicialize CORS in the application
  cors = CORS(app, resources={r"/*": {"origins": "*"}})
# Inicialize service of  Cloudinary
  cloudinary.config( 
    cloud_name = config("CLOUD_NAME"), 
    api_key = config("API_KEY"), 
    api_secret = config("API_SECRET_KEY"),
    secure = True
  )
  # Inicialize service of storage of the credentials of firebase
  key_json=config('KEY')
  url = config('URL_CREDENTIALS_FIREBASE')
  headers = {
    'X-Master-Key': key_json
  }
  req = requests.get(url, json=None, headers=headers)
  data=req.json()["record"]
  
  # Credentials Firebase
  cred = credentials.Certificate(data)
  url=config('URL_FIREBASE')
  
  #Inicialice Firebase
  firebase_admin.initialize_app(cred, {
      'databaseURL': url,
  })