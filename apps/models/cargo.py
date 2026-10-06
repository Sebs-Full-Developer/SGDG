import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cargo(db.Model):
    __tablename__ = 'cargo'
    cargo_id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f'<Cargo {self.titulo}>'
