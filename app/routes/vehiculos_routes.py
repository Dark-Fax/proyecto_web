from flask import Blueprint, render_template, session, redirect, url_for, flash

vehiculos = Blueprint('vehiculos', __name__, url_prefix='/vehiculos')

@vehiculos.route('/listar')
def listar():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    usuario = session['usuario_nombre']
    return render_template('vehiculos/listar.html', usuario_nombre=usuario, titulo_pagina="Catálogo de vehículos eléctricos ⚡")

# Rutas para cada vehículo
@vehiculos.route('/kia')
def kia():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Kia.html', usuario_nombre=session.get('usuario_nombre'), titulo_pagina="Detalles del vehículo ⚡")

@vehiculos.route('/bmw')
def bmw():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_BMW.html', usuario_nombre=session.get('usuario_nombre'), titulo_pagina="Detalles del vehículo ⚡")

@vehiculos.route('/bolt')
def bolt():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Bolt.html', usuario_nombre=session.get('usuario_nombre'), titulo_pagina="Detalles del vehículo ⚡")

@vehiculos.route('/leaf')
def leaf():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Leaf.html', usuario_nombre=session.get('usuario_nombre'), titulo_pagina="Detalles del vehículo ⚡")

@vehiculos.route('/volvo')
def volvo():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Volvo.html', usuario_nombre=session.get('usuario_nombre'), titulo_pagina="Detalles del vehículo ⚡")

@vehiculos.route('/tesla')
def tesla():
    if 'usuario_nombre' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('usuarios.login'))
    return render_template('vehiculos/crear_Tesla.html', usuario_nombre=session.get('usuario_nombre'), titulo_pagina="Detalles del vehículo ⚡")
