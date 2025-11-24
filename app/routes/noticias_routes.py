from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from app import db
from app.models.noticia import Noticia
from functools import wraps
from werkzeug.utils import secure_filename
import os




noticias = Blueprint(
    "noticias",
    __name__,
    url_prefix="/noticias",
)

# -------------------------------
# DECORADORES
# -------------------------------


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_nombre" not in session:
            flash("Debes iniciar sesión", "danger")
            return redirect(url_for("usuarios.login"))
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("rol") != "admin":
            flash("No tienes permisos para esta acción", "danger")
            return redirect(url_for("noticias.listar"))
        return f(*args, **kwargs)

    return decorated_function


# -------------------------------
# RUTAS CRUD NOTICIAS
# -------------------------------


# Listar noticias (todos los usuarios)


@noticias.route("/inicio")
@login_required
def inicio_noticias():
    return render_template(
        "noticias/inicio_noticias.html",
        usuario_nombre=session["usuario_nombre"],
        titulo_pagina="Inicio Noticias"
    )

@noticias.route("/listar")
@login_required
def listar():
    noticias_all = Noticia.query.all()
    return render_template(
        "noticias/listar_noticias.html",
        noticias=noticias_all,
        usuario_nombre=session["usuario_nombre"],
        titulo_pagina="Listado de Noticias 📰",
    )


# Formulario real de creación de noticia (solo admin)
@noticias.route("/crear_formulario", methods=["GET", "POST"])
@login_required
@admin_required 
def crear_formulario():
    if request.method == "POST":
        titulo = request.form["titulo"]
        categoria = request.form["categoria"]
        autor = session.get("usuario_nombre")
        contenido = request.form["contenido"]
        vistas = int(request.form.get("vistas", 0))
        imagen = request.files.get('imagen')  # <-- request.files, no request.form
        filename = None
        if imagen and imagen.filename != '':
            if '.' in imagen.filename and imagen.filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']:
                filename = secure_filename(imagen.filename)
                # Guardar en la carpeta configurada en __init__.py
                save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                
                imagen.save(save_path)
            else:
                flash("Formato de imagen no permitido", "danger")

        nueva_noticia = Noticia(
            titulo=titulo,
            categoria=categoria,
            autor=autor,
            contenido=contenido,
            vistas=vistas,
            imagen=filename,
        )
        db.session.add(nueva_noticia)
        db.session.commit()
        flash("Noticia creada correctamente", "success")
        return redirect(url_for("noticias.listar"))

    return render_template(
        "noticias/crear_noticias_formulario.html",
        usuario_nombre=session["usuario_nombre"],
        titulo_pagina="Crear Noticia ✏️",
    )


# Ver noticia individual (todos los usuarios)
@noticias.route("/ver/<int:id>")
@login_required
def ver(id):
    noticia = Noticia.query.get_or_404(id)
    return render_template(
        "noticias/ver_noticia.html",
        noticia=noticia,
        usuario_nombre=session["usuario_nombre"],
        titulo_pagina=noticia.titulo,
    )


# Editar noticia (solo admin)
@noticias.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def editar(id):
    noticia = Noticia.query.get_or_404(id)
    print("Request method:", request.method)
    print("Form data:", request.form)

    if request.method == "POST":
        # Actualizar campos de texto
        noticia.titulo = request.form["titulo"]
        noticia.categoria = request.form["categoria"]
        noticia.contenido = request.form["contenido"]
        noticia.vistas = int(request.form.get("vistas", noticia.vistas))

        # ---------------------------
        # Procesar la imagen (debug)
        # ---------------------------
        imagen = request.files.get('imagen')
        print("Imagen recibida:", imagen)  # debug
        if imagen and imagen.filename != '':
            filename = secure_filename(imagen.filename)
            ext = filename.rsplit('.', 1)[1].lower()
            print("Nombre seguro:", filename, "Extensión:", ext)
            if ext in current_app.config['ALLOWED_EXTENSIONS']:
                save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                print("Guardando imagen en:", save_path)
                imagen.save(save_path)
                noticia.imagen = filename
                print("Nombre de imagen actualizado en la noticia:", noticia.imagen)
            else:
                flash("Formato de imagen no permitido", "danger")

        # Guardar cambios en la base de datos
        db.session.commit()
        flash("Noticia actualizada correctamente", "success")
        return redirect(url_for("noticias.listar"))

    return render_template(
        "noticias/editar_noticias.html",
        noticia=noticia,
        usuario_nombre=session["usuario_nombre"],
        titulo_pagina="Editar Noticia ✏️",
    )


# Eliminar noticia (solo admin)
@noticias.route("/eliminar/<int:id>", methods=["POST"])
@login_required
@admin_required
def eliminar(id):
    # Evitar que se borren las noticias de prueba
    if id in [1, 2]:
        flash("No se puede eliminar esta noticia de prueba", "info")
        return redirect(url_for("noticias.listar"))

    noticia = Noticia.query.get_or_404(id)
    db.session.delete(noticia)
    db.session.commit()
    flash("Noticia eliminada correctamente", "success")
    return redirect(url_for("noticias.listar"))
