import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estado(db.Model):
    __tablename__ = 'estado'
    estado_id = db.Column(db.Integer, primary_key=True)
    nombre_estado = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.pais_id'), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    # Relación con la tabla pais
    pais = db.relationship('Pais', backref=db.backref('estados', lazy=True))

    def __repr__(self):
        return f'<Estado {self.nombre_estado}>'
