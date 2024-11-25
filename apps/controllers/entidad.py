# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
entidad_bp = Blueprint('entidad', __name__)

@entidad_bp.route('/read_entity')
def read_entity():
    return render_template('read_entity.html')