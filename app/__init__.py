from flask import Config, Flask, jsonify,request
from firebase_admin import db
from firebase_admin import auth ,exceptions
import cloudinary
import cloudinary.uploader
from .config.configuration import inicialize
from .routes.home import home
from .routes.users import users
from .routes.anounces import anounces
from .routes.utils import utils


app = Flask(__name__)
inicialize(app)

app.register_blueprint(home)
app.register_blueprint(users)
app.register_blueprint(utils)
