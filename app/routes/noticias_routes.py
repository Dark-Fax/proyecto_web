from flask import Blueprint, render_template, session, redirect, url_for, flash

noticias = Blueprint("noticias", __name__, url_prefix="/noticias")

@noticias.route("/")
def listar():
    if "usuario_nombre" not in session:
        flash("Debes iniciar sesión", "danger")
        return redirect(url_for("usuarios.login"))
    return render_template("noticias/listar_Noticias.html")

@noticias.route("/crear")
def crear():
    if "usuario_nombre" not in session:
        flash("Debes iniciar sesión", "danger")
        return redirect(url_for("usuarios.login"))
    nombre_usuario = session["usuario_nombre"]
    return render_template("noticias/crear_Noticias.html", usuario_nombre=nombre_usuario)

@noticias.route("/editar/<int:id>")
def editar(id):
    if "usuario_nombre" not in session:
        flash("Debes iniciar sesión", "danger")
        return redirect(url_for("usuarios.login"))
    return render_template("noticias/editar_Noticias.html", id=id)
