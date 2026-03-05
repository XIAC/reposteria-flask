from app import create_app
from app.models import User, Producto
from app.extensions import db

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Producto': Producto}

if __name__ == '__main__':
    app.run()
