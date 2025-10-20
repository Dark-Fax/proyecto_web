from app import db

#Modelo de ejemplo 
class Usuario(db.Model): #Definimos una clase llamada 'Usuario',
    #que heredara de db.Model y hara un mapeo con una tabla de la DB


    #Definimos un id con formato Integer el cual sera su llave primaria [PK]
    id = db.Column(db.Integer, primary_key=True)
    #nombre que sera un String de longitud 100 y que no puede ser null
    nombre = db.Column(db.String(100), nullable=False)