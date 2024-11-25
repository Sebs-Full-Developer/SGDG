# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
asignacion_cargo_bp = Blueprint('asignacion_cargo', __name__)

@asignacion_cargo_bp.route('/read_set_ocupation')
def read_set_ocupation():
    return render_template('read_set_ocupation.html')