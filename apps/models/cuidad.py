import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    ciudad_id = db.Column(db.Integer, primary_key=True)
    nombre_ciudad = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.estado_id'), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    # Relación con la tabla estado
    estado = db.relationship('Estado', backref=db.backref('ciudades', lazy=True))

    def __repr__(self):
        return f'<Ciudad {self.nombre_ciudad}>'
