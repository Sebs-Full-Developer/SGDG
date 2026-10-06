from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para las ciudades
ciudad_bp = Blueprint('ciudad', __name__)

@ciudad_bp.route('/read_city')
def read_city():
    """Lee todos los registros de la tabla 'ciudad' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todas las ciudades
        cursor.execute("{CALL proc_select_ciudad()}")
        ciudades = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not ciudades:
            ciudades = []

    except Exception as e:
        ciudades = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de las ciudades
    return render_template('ciudad/read_city.html', ciudades=ciudades)

@ciudad_bp.route('/ciudad/create_city')
def create_city():
    return render_template('ciudad/create_city.html')

@ciudad_bp.route('/ciudad/delete_city')
def delete_city():
    return render_template('ciudad/delete_city.html')

@ciudad_bp.route('/ciudad/update_city')
def update_city():
    return render_template('ciudad/update_city.html')