# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/read_user')
def read_user():
    return render_template('read_user.html')