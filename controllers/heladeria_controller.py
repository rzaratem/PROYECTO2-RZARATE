from models.heladeria import Ingrediente,Producto
from flask import jsonify, Blueprint
from db import db

from flask import render_template, request, flash, redirect, url_for, session,  jsonify

PATH_URL = "Proyecto_Heladeria_Web/views"

#user_blueprint = Blueprint('user_bp', __name__, url_prefix="/users")
heladeria_blueprint = Blueprint('heladeria_bp', __name__)

@heladeria_blueprint.route('/')
def index():
    return "Este es la ruta inicial"

""" @heladeria_blueprint.route('/update')
def update():
    return "Este es una ruta para heladeria" """

def heladerias_routes(app):
    @app.route('/')
    def index():
        return render_template ("index.html")
        #return "Esta es la App de HELADERIA"

##################################################
#@user_blueprint.route('/lista')
#def lista():
#    users=User.query.all()
#    return jsonify({"data": users[1].name}),201 


""" @heladeria_blueprint.route('/list')
def list():
    heladerias =Heladeria.query.all()
    return jsonify({"data": heladerias[1].name}),201 

 """



@heladeria_blueprint.route('/ingredientes')
def listar_ingredientes():
    ingredientes = Ingrediente.query.all()
    #return render_template("listar_users.html",listar)
    return render_template ("listar_ingredientes.html",ingredientes=ingredientes) # ("listar_users.html",heladerias=heladerias)


@heladeria_blueprint.route('/productos')
def listar_productos():
    productos = Producto.query.all()
    #return render_template("listar_users.html",listar)
    return render_template ("listar_productos.html",productos=productos) # ("listar_users.html",heladerias=heladerias)




@heladeria_blueprint.route('/update')
def update():
    return "Ruta para actualizar"

