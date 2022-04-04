import cloudinary
from decouple import config
import requests
import firebase_admin
from firebase_admin import credentials

# Inicializar Cloudinary
cloudinary.config( 
  cloud_name = config("CLOUD_NAME"), 
  api_key = config("API_KEY"), 
  api_secret = config("API_SECRET_KEY"),
  secure = True
)
# Inicializar JSONBin
key_json=config('KEY')
url = config('URL_CREDENTIALS_FIREBASE')
headers = {
  'X-Master-Key': key_json
}
req = requests.get(url, json=None, headers=headers)
data=req.json()["record"]

# Credenciales Firebase
cred = credentials.Certificate(data)
url=config('URL_FIREBASE')

#Inicializar Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': url,
})