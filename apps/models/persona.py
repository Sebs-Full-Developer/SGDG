import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = 'persona'
    persona_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.user_id'), nullable=True)
    nombre_persona = db.Column(db.String(100), nullable=False)
    apellido_persona = db.Column(db.String(100), nullable=False)
    documento_identidad = db.Column(db.String(50), unique=True, nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('genero.genero_id'), nullable=False)
    ciudad_id = db.Column(db.Integer, db.ForeignKey('ciudad.ciudad_id'), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    direccion_persona = db.Column(db.String(255), nullable=True)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    # Relaciones con otras tablas
    usuario = db.relationship('Usuario', backref=db.backref('personas', lazy=True))
    genero = db.relationship('Genero', backref=db.backref('personas', lazy=True))
    ciudad = db.relationship('Ciudad', backref=db.backref('personas', lazy=True))

    def __repr__(self):
        return f'<Persona {self.nombre_persona} {self.apellido_persona}>'
