from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv



import urllib
import os


# Inicializamos la base de datos (sin app todavía)
db = SQLAlchemy()
# y las migraciones 
migrate = Migrate()

def create_app():
    #Crearemos la app Flask 
    app = Flask(__name__)
    app.secret_key = 'supersecreto'

    #Cargar las variables del .env
    load_dotenv()
    
    
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


    #Inicializamos SQLAlchemy con Flask
    db.init_app(app)
    #Y la extension de la migracion 
    migrate.init_app(app, db)

    #Importamos y registraremos las rutas 
    from app.routes.main_routes import main 
    from app.routes.usuarios_routes import usuarios
    from app.routes.vehiculos_routes import vehiculos
    
    app.register_blueprint(main)     
    app.register_blueprint(usuarios)   
    app.register_blueprint(vehiculos)
                                       
    return app                          