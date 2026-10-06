import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Telefono(db.Model):
    __tablename__ = 'telefono'
    telefono_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id'), nullable=False)
    tipo_telefono = db.Column(db.String(50), nullable=False)
    numero_telefono = db.Column(db.String(20), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    # Relación con la tabla persona
    persona = db.relationship('Persona', backref=db.backref('telefonos', lazy=True))

    def __repr__(self):
        return f'<Telefono {self.numero_telefono}>'
