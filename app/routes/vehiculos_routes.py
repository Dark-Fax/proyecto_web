from flask import Blueprint, render_template, session, redirect, url_for, flash

vehiculos = Blueprint('vehiculos', __name__, url_prefix='/vehiculos')

@vehiculos.route('/listar')
def listar():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    usuario = session['usuario_nombre']
    return render_template('vehiculos/listar.html', usuario_nombre=usuario)

# Rutas para cada vehículo
@vehiculos.route('/kia')
def kia():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Kia.html')

@vehiculos.route('/bmw')
def bmw():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_BMW.html')

@vehiculos.route('/bolt')
def bolt():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Bolt.html')

@vehiculos.route('/leaf')
def leaf():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Leaf.html')

@vehiculos.route('/volvo')
def volvo():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Volvo.html')

@vehiculos.route('/tesla')
def tesla():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Tesla.html')
