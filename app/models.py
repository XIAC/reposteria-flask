from flask_login import UserMixin
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True ,nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(100), default="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_venta = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Producto {self.nombre}>'