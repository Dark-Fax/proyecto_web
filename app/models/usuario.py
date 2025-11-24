from app import db
from werkzeug.security import generate_password_hash, check_password_hash

#Modelo de ejemplo 
class Usuario(db.Model): #Definimos una clase llamada 'Usuario',
    #que heredara de db.Model y hara un mapeo con una tabla de la DB
    __tablename__ = 'usuarios'


    #Definimos un id con formato Integer el cual sera su llave primaria [PK]
    id = db.Column(db.Integer, primary_key=True)
    #nombre que sera un String de longitud 100 y que no puede ser null
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    #email que sera un String de longitud 70 y que no puede ser null, ademas de ser unico
    email = db.Column(db.String(70), unique=True, nullable=False)
    #password que sera un String de longitud 50 y que no puede ser null
    password_hash = db.Column(db.String(512), nullable=True)
    password = db.Column(db.String(50), nullable=True)        # Antigua (solo temporal)
    #telefono que sera un String de longitud 10 y que no puede ser null
    telefono = db.Column(db.String(10), nullable=False)

    #Nuevo, rol de usuario (admin o usuario)    -----> nueva agregacion  
    rol = db.Column(db.String(50), nullable=False, default="usuario")

    # ✅ Guardar la contraseña encriptada
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # ✅ Verificar contraseña (durante login)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f"<Usuario {self.email}>"