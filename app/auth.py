from  flask import Blueprint, redirect, url_for, render_template, request
from flask_login import login_required, login_user, logout_user
from .models  import User, Producto
from  .extensions import login_manager
from flask import jsonify
from .ai_chat import preguntar_chatbot

auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@auth_bp.route('/')
def inicio():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods = ['GET','POST']) 
def login():
    if request.method == "POST":
        usuario = User.query.filter_by(
            username = request.form.get("nombreusuario")
        ).first()
        
        if usuario and usuario.check_password(request.form.get("contrasenia")):
            login_user(usuario)
            return redirect("/admin")
    
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

# chatbot

@auth_bp.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    pregunta = data.get("mensaje")
    respuesta = preguntar_chatbot(pregunta)
    return jsonify({
        "respuesta": respuesta
    })
@auth_bp.route("/chat")
def chat():

    return render_template("chatbot.html")   
# analisis ia con graficos
from .models import Producto
from .extensions import db
from sqlalchemy import func
from .ai_chat import client
@auth_bp.route("/dashboard")
@login_required
def dashboard():
    total_productos = Producto.query.count()
    valor_stock = db.session.query(func.sum(Producto.precio * Producto.stock)).scalar()
    productos = Producto.query.all()
    nombres = [ prod.nombre for prod in productos]
    stock = [ prod.stock for prod in productos]
    return render_template("dashboard.html", 
                          total_productos =  total_productos,
                          valor_stock = valor_stock,
                          nombres = nombres,
                          stock = stock)
    
@auth_bp.route("/analisis-ia")
def analisis_ia ():
    productos = Producto.query.all()
    lista = ""
    for  p in productos:
        lista += f"{p.nombre}, stock: {p.stock} , precio: {p.precio}\n"
    
    prompt = f" Analiza los siguientes productos de repostería {lista} usando nombre, stock y ventas. Identifica productos con stock bajo y stock alto, productos más vendidos y genera recomendaciones para ventas."
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    generated_text = response.choices[0].message.content
    return jsonify({"analisis": generated_text})
