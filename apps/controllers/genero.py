# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
genero_bp = Blueprint('genero', __name__)

@genero_bp.route('/read_gender')
def read_gender():
    return render_template('genero/read_gender.html')