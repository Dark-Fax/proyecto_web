from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models.usuario import Usuario

cuenta = Blueprint("cuenta", __name__, template_folder="../templates/usuarios")

@cuenta.route("/cuenta")
def ver_cuenta():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión primero", "danger")
        return redirect(url_for("usuarios.login"))

    usuario = Usuario.query.get(session["usuario_id"])
    return render_template("usuarios/cuenta.html", usuario=usuario, usuario_nombre=usuario.nombre, titulo_pagina="Configuración de Cuenta 👤")

@cuenta.route("/cuenta/editar", methods=["POST"])
def editar_cuenta():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión primero", "danger")
        return redirect(url_for("usuarios.login"))

    usuario = Usuario.query.get(session["usuario_id"])
    usuario.nombre = request.form["nombre"]
    usuario.telefono = request.form["telefono"]
    usuario.email = request.form["email"]

    nueva_contrasena = request.form.get("nueva_contrasena", "").strip()
    if nueva_contrasena:
        usuario.set_password(nueva_contrasena)
        flash("Contraseña actualizada correctamente 🔒", "success")
    else:
        flash("Datos actualizados correctamente ✅", "success")

    db.session.commit()
    return redirect(url_for("cuenta.ver_cuenta"))

@cuenta.route("/cuenta/eliminar", methods=["POST"])
def eliminar_cuenta():
    if "usuario_id" not in session:
        return redirect(url_for("usuarios.login"))

    usuario = Usuario.query.get(session["usuario_id"])
    db.session.delete(usuario)
    db.session.commit()
    session.clear()

    flash("Tu cuenta ha sido eliminada permanentemente", "info")
    return redirect(url_for("usuarios.registro"))