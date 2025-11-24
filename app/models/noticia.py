from app import db
from datetime import datetime

class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(100))
    autor = db.Column(db.String(100))
    contenido = db.Column(db.Text, nullable=False)
    vistas = db.Column(db.Integer, default=0)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    imagen = db.Column(db.String(255), nullable=True)
