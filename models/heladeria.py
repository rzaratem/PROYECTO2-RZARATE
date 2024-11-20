from db import db
from sqlalchemy import text

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250), nullable = False, unique = True)
    precio = db.Column(db.Integer, nullable = False)
    calorias = db.Column(db.Integer, nullable = False)
    inventario = db.Column(db.Integer, nullable = False)
    es_vegetariano = db.Column(db.String(2), nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'), onupdate = db.func.current_timestamp())



class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre_producto = db.Column(db.String(120), nullable = False, unique = True)
    tipo_producto = db.Column(db.String(100), nullable = False)
    calorias = db.Column(db.String(50), nullable = False)
    costo = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, nullable = False, default = db.func.current_timestamp(), server_default=text('CURRENT_TIMESTAMP'), onupdate = db.func.current_timestamp())


