from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para las claves
clave_bp = Blueprint('clave', __name__)

@clave_bp.route('/read_key')
def read_key():
    """Lee todos los registros de la tabla 'clave' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todas las claves
        cursor.execute("{CALL proc_select_clave()}")
        claves = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not claves:
            claves = []

    except Exception as e:
        claves = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de las claves
    return render_template('clave/read_key.html', claves=claves)

@clave_bp.route('/clave/create_key')
def create_key():
    return render_template('clave/create_key.html')

@clave_bp.route('/clave/delete_key')
def delete_key():
    return render_template('clave/delete_key.html')

@clave_bp.route('/clave/update_key')
def update_key():
    return render_template('clave/update_key.html')