

#Inicializaremos la base de datos
db = SQLAlchemy(app)



#Ruta principal 
@app.route('/')
def home():
    return"<h1> Hola, Flask esta funcionando correctamente </h1>"

#Ejecutar el servidor local 
if __name__ == "__main__":
    app.run(debug=True)  