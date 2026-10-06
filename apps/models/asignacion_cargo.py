import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AsignacionCargo(db.Model):
    __tablename__ = 'asignacion_cargo'
    asignacion_id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id'), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.cargo_id'), nullable=False)
    entidad_id = db.Column(db.Integer, db.ForeignKey('entidad.entidad_id'), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(50), default='Activo')
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    # Relaciones con otras tablas
    persona = db.relationship('Persona', backref=db.backref('asignaciones_cargo', lazy=True))
    cargo = db.relationship('Cargo', backref=db.backref('asignaciones_cargo', lazy=True))
    entidad = db.relationship('Entidad', backref=db.backref('asignaciones_cargo', lazy=True))

    def __repr__(self):
        return f'<AsignacionCargo {self.cargo_id} - {self.entidad_id}>'
