# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
ciudad_bp = Blueprint('ciudad', __name__)

@ciudad_bp.route('/read_city')
def read_city():
    return render_template('read_city.html')