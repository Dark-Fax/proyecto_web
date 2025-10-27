# app/routes/noticias_routes.py
from flask import Blueprint, render_template

noticias = Blueprint('noticias', __name__, url_prefix='/noticias')

@noticias.route('/')
def listar():
    return render_template('noticias/listar_Noticias.html')

@noticias.route('/crear')
def crear():
    return render_template('noticias/crear_Noticias.html')

@noticias.route('/editar/<int:id>')
def editar(id):
    return render_template('noticias/editar_Noticias.html', id=id)
