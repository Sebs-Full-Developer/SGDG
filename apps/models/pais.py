import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    pais_id = db.Column(db.Integer, primary_key=True)
    nombre_pais = db.Column(db.String(100), default='Colombia', nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f'<Pais {self.nombre_pais}>'
