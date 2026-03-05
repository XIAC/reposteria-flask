import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
# 1. Agregamos 'migrate' a las extensiones
from .extensions import db, login_manager, admin, migrate 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicialización de extensiones
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    
    # 2. Inicializamos las migraciones vinculándolas a app y db
    migrate.init_app(app, db)
    
    from .models import User
    from .admin import configuracion_admin
    from .auth import auth_bp
    
    # 3. CORRECCIÓN: Pasamos 'app' a la configuración del admin
    configuracion_admin(app) 
    
    app.register_blueprint(auth_bp)
    
    return app