from app import create_app
from app.extensions import db
from app.models import User
app = create_app()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            admin_user = User(username="admin", role="admin")
            admin_user.set_password("1234")  # contraseña hasheada
            db.session.add(admin_user)
            db.session.commit()
            print("Usuario admin creado correctamente")
    app.run(debug=True)