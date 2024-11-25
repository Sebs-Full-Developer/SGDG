import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Clave(db.Model):
    __tablename__ = 'clave'
    username = db.Column(db.String(50), db.ForeignKey('usuario.username'), unique=True, nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=False)
    
    # Relación con la tabla usuario
    usuario = db.relationship('Usuario', backref=db.backref('clave', uselist=False))
    
    def __repr__(self):
        return f'<Clave {self.username}>'
