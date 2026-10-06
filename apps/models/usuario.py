import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return f'<Usuario {self.username}>'
