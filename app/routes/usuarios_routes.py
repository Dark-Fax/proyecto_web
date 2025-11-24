# Aqui se definiran las rutas que manejaran el registro e inicio de sesion de los usuarios

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models.usuario import Usuario  # Aqui importaremos el modelo de Usuario

usuarios = Blueprint("usuarios", __name__, template_folder="../templates/usuarios")


# Registro
@usuarios.route("/register", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["usuario"]
        correo = request.form["email"]
        contrasena = request.form["password"]
        telefono = request.form["telefono"]

        # Verificar que se reciban correctamente
        if not nombre or not correo or not contrasena or not telefono:
            flash("Todos los campos son obligatorios", "danger")
            return redirect(url_for("usuarios.registro"))

        # Verificar si el usuario y email ya existe
        if Usuario.query.filter_by(nombre=nombre).first():
            flash("Este nombre de usuario ya está registrado 😕", "danger")
            return redirect(url_for("usuarios.registro"))
        if Usuario.query.filter_by(email=correo).first():
            flash("Este correo ya está registrado 📧", "danger")
            return redirect(url_for("usuarios.registro"))

        nuevo_usuario = Usuario(
            nombre=nombre, email=correo, telefono=telefono, rol="usuario"
        )
        nuevo_usuario.set_password(contrasena)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Usuario registrado correctamente", "success")
        return redirect(url_for("usuarios.login"))

    return render_template("usuarios/register.html")


# Login de los usuarios


@usuarios.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario_ingresado = request.form.get("usuario", "").strip()
        contrasena = request.form.get("password", "").strip()

        # Verificaremos el usuario y contraseña en la base de datos
        usuario = Usuario.query.filter_by(nombre=usuario_ingresado).first()
        if usuario and usuario.check_password(contrasena):
            session["usuario_id"] = usuario.id
            session["usuario_nombre"] = usuario.nombre
            session["rol"] = usuario.rol
            flash(f"Bienvenido {usuario.nombre}!", "success")
            return redirect(
                url_for("noticias.inicio_noticias")
            )  # Redirige al Dashboard
        else:
            flash("Correo o contraseña incorrectos", "danger")
            return redirect(url_for("usuarios.login"))

    return render_template("usuarios/login.html")


# Logout
@usuarios.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente", "sucess")
    return redirect(url_for("usuarios.login"))
