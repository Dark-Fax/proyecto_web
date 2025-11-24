from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import urllib.parse
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecreto'

    # 1. Cargar las variables del .env
    load_dotenv()
    
    # 2. Leer credenciales de Azure desde el .env
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    
    # Driver: Azure suele usar el 17 o el 18.
    driver = 'ODBC Driver 17 for SQL Server'

    # 3. Armar la cadena de conexión para AZURE
    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    
    params = urllib.parse.quote_plus(connection_string)
    
    print("--- CONECTANDO A AZURE ---")
    print(f"Servidor: {server}")
    print(f"Usuario: {username}")
    print("--------------------------")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 



    # === Configuración para subir imágenes ===
    UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'img', 'noticias')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # crea la carpeta si no existe
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


    #Inicializamos SQLAlchemy con Flask

    db.init_app(app)
    migrate.init_app(app, db)

    # Importar rutas
    from app.routes.main_routes import main 
    from app.routes.usuarios_routes import usuarios
    from app.routes.vehiculos_routes import vehiculos
    from app.routes.noticias_routes import noticias
    from app.routes.calculadora_routes import calculadora
    from app.routes.cuenta_routes import cuenta 
    from app.routes.mapa_routes import mapa  # <--- 1. AGREGAR ESTO (Importar)
    
    app.register_blueprint(main)     
    app.register_blueprint(usuarios)   
    app.register_blueprint(vehiculos)
    app.register_blueprint(noticias)
    print("Blueprint noticias cargado")
    app.register_blueprint(calculadora)
    app.register_blueprint(cuenta)
    app.register_blueprint(mapa)         # <--- 2. AGREGAR ESTO (Registrar)

    return app



