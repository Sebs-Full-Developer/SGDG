from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para los estados
estado_bp = Blueprint('estado', __name__)

@estado_bp.route('/read_state')
def read_state():
    """Lee todos los registros de la tabla 'estado' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todos los estados
        cursor.execute("{CALL proc_select_estado()}")
        estados = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not estados:
            estados = []

    except Exception as e:
        estados = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de los estados
    return render_template('estado/read_state.html', estados=estados)

@estado_bp.route('/estado/create_state')
def create_state():
    return render_template('estado/create_state.html')

@estado_bp.route('/estado/delete_state')
def delete_state():
    return render_template('estado/delete_state.html')

@estado_bp.route('/estado/update_state')
def update_state():
    return render_template('estado/update_state.html')