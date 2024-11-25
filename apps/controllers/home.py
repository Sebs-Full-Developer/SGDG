# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    return render_template('home.html')  # Página de inicio o cualquier vista que quieras mostrar
