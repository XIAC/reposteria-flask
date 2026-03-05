import pymysql
from flask import Flask
from config import Config
from .extensions import db, login_manager, admin, migrate
from .auth import auth_bp
from .admin_views import configuracion_admin
pymysql.install_as_MySQLdb()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)
    app.register_blueprint(auth_bp)
    with app.app_context():
        configuracion_admin()
    return app