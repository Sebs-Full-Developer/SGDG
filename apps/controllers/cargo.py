# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/read_ocupation')
def read_ocupation():
    return render_template('read_ocupation.html')