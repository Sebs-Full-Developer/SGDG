import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entidad(db.Model):
    __tablename__ = 'entidad'
    entidad_id = db.Column(db.Integer, primary_key=True)
    entidad_id = db.Column(SQLAlchemy.Integer, primary_key=True)
    nombre_entidad = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    tipo_entidad = db.Column(db.String(50), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f'<Entidad {self.nombre_entidad}>'
