# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
pais_bp = Blueprint('pais', __name__)

@pais_bp.route('/read_country')
def read_country():
    return render_template('read_country.html')