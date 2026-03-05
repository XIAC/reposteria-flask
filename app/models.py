from flask_login import UserMixin
from .extensions import db, login_manager # <--- AGREGA 'login_manager' AQUÍ
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    # ... (todo tu código anterior de la clase User se queda igual)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True ,nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(100), default="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    from .extensions import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))