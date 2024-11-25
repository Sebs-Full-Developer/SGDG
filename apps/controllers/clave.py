# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
clave_bp = Blueprint('clave', __name__)

@clave_bp.route('/read_key')
def read_key():
    return render_template('read_key.html')