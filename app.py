from flask import Flask
from dotenv import load_dotenv
from db import db, init_db
from models.heladeria import Ingrediente,Producto
from controllers.heladeria_controller import heladeria_blueprint
from controllers.heladeria_controller import heladerias_routes
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import os
load_dotenv()
#app = Flask(__name__)
app=Flask(__name__,template_folder='views')





#app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_STRING_CONNECTION')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print(app.config["SQLALCHEMY_DATABASE_URI"])

#db=SQLAlchemy(app)
db.init_app(app)
init_db(app)

heladerias_routes(app)

#class User(db.Model):
#   __tablename__ ='users'
#   id=db.Column(db.Integer, primary_key=True)
  
app.register_blueprint(heladeria_blueprint)  
  
  #def init_db(app):
if __name__ == '__main__':
    app.run(debug=True)

""" @app.route('/')
def index():
    return "Hello world!"
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True) """