from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

import urllib
import os
from dotenv import load_dotenv

#Cargar las variables del .env
load_dotenv()

#Crearemos la app Flask 
app = Flask(__name__)

#Aqui crearemos la conexion usando la autenticacion de Windows 
#Armamos una cadena de conexion llamada (connection string)
params = urllib.parse.quote_plus( #urllib.parse.quote_plus --> sirve para codificar correctamente la cadena y evita errores con caracteres especiales cuando se pase al conector pyodbc
    #en otras palabras establecemos la direccion y parametros que Flask usara para comunciarse con SQL Server
    
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"  #Indica el driver ODBC que usara python para hablar con SQL Server
    f"SERVER={os.getenv('DB_SERVER')};" #Usa el valor de la variable DB_SERVER guardada en el archivo .env (localhost)
    f"DATABASE={os.getenv('DB_NAME')};" #El nombre de la DB (Proyecto_web)
    f"Trusted_Connection=yes;" #Esto activara la autenticación de Windows (sin pedir permiso, ni contraseña)
)

#Aqui le explicamos donde esta la base de datos a Flask 
#usamos 'mssql+pyodbc' el cual es el motor para DB's SQL Server
#y despues que se conecte con los parametros que derfinimos en 'params'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #--> Desactivaremos una caracteristica de SQLAlchemy 
#TRACK_MODIFICATIONS monitorea cada cambio en los objetos, tenerlo asi ahorra memoria y evita advertencias innecesarias


#Inicializaremos la base de datos
db = SQLAlchemy(app)

#Modelo de ejemplo 
class Usuario(db.Model): #Definimos una clase llamada 'Usuario',
    #que heredara de db.Model y hara un mapeo con una tabla de la DB


    #Definimos un id con formato Integer el cual sera su llave primaria [PK]
    id = db.Column(db.Integer, primary_key=True)
    #nombre que sera un String de longitud 100 y que no puede ser null
    nombre = db.Column(db.String(100), nullable=False)

#Ruta principal 
@app.route('/')
def home():
    return"<h1> Hola, Flask esta funcionando correctamente </h1>"

#Ejecutar el servidor local 
if __name__ == "__main__":
    app.run(debug=True)