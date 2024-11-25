# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
persona_bp = Blueprint('persona', __name__)

@persona_bp.route('/read_person')
def read_person():
    return render_template('read_person.html')