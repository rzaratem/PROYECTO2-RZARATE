from models.user import User
from flask import jsonify, Blueprint
from db import db

from flask import render_template, request, flash, redirect, url_for, session,  jsonify

PATH_URL = "Taller2_Modulo2/views"

#user_blueprint = Blueprint('user_bp', __name__, url_prefix="/users")
user_blueprint = Blueprint('user_bp', __name__)

@user_blueprint.route('/')
def index():
    return "Este es la ruta inicial"

@user_blueprint.route('/update')
def update():
    return "Este es una ruta para actualizar usuarios"

def users_routes(app):
    @app.route('/')
    def index():
        return "Esta es la App de usuarios"

##################################################
#@user_blueprint.route('/lista')
#def lista():
#    users=User.query.all()
#    return jsonify({"data": users[1].name}),201 


@user_blueprint.route('/list')
def list():
    users =User.query.all()
    return jsonify({"data": users[1].name}),201 





@user_blueprint.route('/listar')
def listar():
    users =User.query.all()
    #return render_template("listar_users.html",listar)
    return render_template ("listar_users.html",users=users)

    #return jsonify.query
    #result = db.session.execute(query)
    #return jsonify({"data": query[1].name}),201 
    #User = result.scalars()

#listar=db.session.query(db.users).all()
    #query = User.select(User)
    #return listar


    #result = db.session.execute(query)
    #users = result.scalars()
    #return jsonify({"data": User[1].name}),201 

@user_blueprint.route('/usuarios')
def upda():
    return "Usuarios Este es una ruta para actualizar usuarios"

""" def users_routes (app):
    @app.route('/usuarios2')
    def list():
        users=User.query.all()
    return jsonify({"data": users[1].name}),201 """