# home.py
from flask import Blueprint, render_template

# Crear un blueprint para el home
telefono_bp = Blueprint('telefono', __name__)

@telefono_bp.route('/read_cellphone')
def read_cellphone():
    return render_template('read_cellphone.html')