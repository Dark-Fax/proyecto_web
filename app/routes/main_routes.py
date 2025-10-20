#Esta sera la ruta prinicpal de la pagina 'Home'
from flask import Blueprint, render_template, session, redirect, url_for, flash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    #Redirige al dashboard si el usuario ya inició sesión
    if 'usuario_nombre' in session:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('usuarios.login'))

@main.route('/dashboard')
def dashboard():
    #erificamos que el usuario este logueado
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    
    #Pasar el nombre de usuario al template 
    nombre_usuario = session['usuario_nombre']
    return render_template('usuarios/dashboard.html', usuario_nombre=nombre_usuario)