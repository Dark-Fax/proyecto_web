from flask import Blueprint, render_template, session, redirect, url_for, flash


vehiculos = Blueprint('vehiculos', __name__, url_prefix='/vehiculos')

@vehiculos.route('/listar')
def listar():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    

    usuario = session['usuario_nombre']
    return render_template('vehiculos/listar.html', usuario_nombre=usuario)