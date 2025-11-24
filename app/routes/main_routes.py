from flask import Blueprint, session, redirect, render_template, url_for, flash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Si el usuario ya inició sesión, lo mandamos directo a crear noticias
    if 'usuario_nombre' in session:
        return redirect(url_for('noticias.crear_formulario'))
    return redirect(url_for('usuarios.login'))

# Mantener /dashboard para otras secciones que no sean noticias
@main.route('/dashboard')
def dashboard():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))

    # Solo renderiza dashboard si quieres mostrar algo
    return render_template('usuarios/dashboard.html', usuario_nombre=session['usuario_nombre'])
