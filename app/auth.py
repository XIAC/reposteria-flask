from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from .models import User
from .extensions import login_manager
auth_bp = Blueprint("auth", __name__)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@auth_bp.route('/')
def inicio():
    if current_user.is_authenticated:
        return redirect("/admin")
    return redirect(url_for('auth.login'))
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect("/admin")
    if request.method == "POST":
        nombre = request.form.get("nombreusuario").strip()
        contrasenia = request.form.get("contrasenia").strip()
        usuario = User.query.filter_by(username=nombre).first()
        if usuario:
            print("Check password:", usuario.check_password(contrasenia))
        if usuario and usuario.check_password(contrasenia):
            login_user(usuario)
            return redirect("/admin")
        else:
            flash("Usuario o contraseña incorrecta")
    return render_template("login.html")
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))