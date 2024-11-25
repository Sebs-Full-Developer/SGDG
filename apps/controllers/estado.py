# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
estado_bp = Blueprint('estado', __name__)

@estado_bp.route('/read_state')
def read_state():
    return render_template('read_state.html')