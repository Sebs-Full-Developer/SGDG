import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Genero(db.Model):
    __tablename__ = 'genero'
    genero_id = db.Column(db.Integer, primary_key=True)
    nombre_genero = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f'<Genero {self.nombre_genero}>'
