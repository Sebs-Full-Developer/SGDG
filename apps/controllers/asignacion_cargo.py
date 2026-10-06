from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para la asignación de cargos
asignacion_cargo_bp = Blueprint('asignacion_cargo', __name__)

@asignacion_cargo_bp.route('/read_set_ocupation')
def read_set_ocupation():
    """Lee todos los registros de la tabla 'asignacion_cargo' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todas las asignaciones de cargos
        cursor.execute("{CALL proc_select_asignacion_cargo()}")
        asignaciones = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not asignaciones:
            asignaciones = []

    except Exception as e:
        asignaciones = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de las asignaciones de cargos
    return render_template('asignacion_cargo/read_set_ocupation.html', asignaciones=asignaciones)

@asignacion_cargo_bp.route('/asignacion_cargo/create_set_ocupation')
def create_set_ocupation():
    return render_template('asignacion_cargo/create_set_ocupation.html')

@asignacion_cargo_bp.route('/asignacion_cargo/delete_set_ocupation')
def delete_set_ocupation():
    return render_template('asignacion_cargo/delete_set_ocupation.html')

@asignacion_cargo_bp.route('/asignacion_cargo/update_set_ocupation')
def update_set_ocupation():
    return render_template('asignacion_cargo/update_set_ocupation.html')