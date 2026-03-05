from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate  # <--- Agregamos esto

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name="Panel Administrador")
migrate = Migrate()  # <--- Creamos la instancia de Migrate
login_manager.login_view = "auth.login" # Ajustado para que coincida con tu Blueprint