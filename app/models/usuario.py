from app import db

#Modelo de ejemplo 
class Usuario(db.Model): #Definimos una clase llamada 'Usuario',
    #que heredara de db.Model y hara un mapeo con una tabla de la DB
    __tablename__ = 'usuarios'


    #Definimos un id con formato Integer el cual sera su llave primaria [PK]
    id = db.Column(db.Integer, primary_key=True)
    #nombre que sera un String de longitud 100 y que no puede ser null
    nombre = db.Column(db.String(100), nullable=False)
    #email que sera un String de longitud 70 y que no puede ser null, ademas de ser unico
    email = db.Column(db.String(70), unique=True, nullable=False)
    #password que sera un String de longitud 50 y que no puede ser null
    password = db.Column(db.String(50), nullable=False)
    #telefono que sera un String de longitud 10 y que no puede ser null
    telefono = db.Column(db.String(10), nullable=False)


    def __repr__(self):
        return f"<Usuario {self.email}>"