#Aqui se definiran las rutas que manejaran el registro e inicio de sesion de los usuarios

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db 
from app.models.usuario import Usuario #Aqui importaremos el modelo de Usuario

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/register', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['usuario']
        correo = request.form['email']
        contrasena = request.form['password']
        telefono = request.form['telefono']
        

        # Verificar que se reciban correctamente
        if not nombre or not correo or not contrasena or not telefono:
            flash('Todos los campos son obligatorios', 'danger')
            return redirect(url_for('usuarios.registro'))

        #Verificar si el usuario ya existe 
        usuario_existente = Usuario.query.filter_by(nombre=nombre).first()
        if usuario_existente:
            flash('Este nombre de usuario ya esta registrado', 'danger')
            return redirect(url_for('usuarios.registro'))
        
        #Verificar si el correo ya existe 
        email_existente = Usuario.query.filter_by(email=correo).first()
        if email_existente:
            flash('Este correo ya esta registrado', 'danger')
            return redirect(url_for('usuarios.registro'))

        nuevo_usuario = Usuario(
            nombre=nombre,
            email=correo,
            telefono=telefono,
            password=contrasena
        )

        db.session.add(nuevo_usuario)
        db.session.commit()


        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('usuarios.login'))
    
        
    
    return render_template('usuarios/register.html')


#Login de los usuarios 

@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_ingresado = request.form.get('usuario', '').strip()
        contrasena = request.form.get('password', '').strip()

        #Verificaremos el usuario y contraseña en la base de datos 
        usuario = Usuario.query.filter_by(nombre=usuario_ingresado, password=contrasena).first()
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            flash(f'Bienvenido {usuario.nombre}!', 'success')
            return redirect(url_for('main.home')) #Redirige al home o Dashboard
        else:
            flash('Correo o contraseña incorrectos', 'danger')
            return redirect(url_for('usuarios.login'))
        
    return render_template('usuarios/login.html')

@usuarios.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'sucess')
    return redirect(url_for('usuarios.login'))