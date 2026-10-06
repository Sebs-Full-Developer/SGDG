from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para los cargos
cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/read_ocupation')
def read_ocupation():
    """Lee todos los registros de la tabla 'cargo' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todos los cargos
        cursor.execute("{CALL proc_select_cargo()}")
        cargos = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not cargos:
            cargos = []

    except Exception as e:
        cargos = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de los cargos
    return render_template('cargo/read_ocupation.html', cargos=cargos)

@cargo_bp.route('/cargo/create_ocupation')
def create_ocupation():
    return render_template('cargo/create_ocupation.html')

@cargo_bp.route('/cargo/delete_ocupation')
def delete_ocupation():
    return render_template('cargo/delete_ocupation.html')

@cargo_bp.route('/cargo/update_ocupation')
def update_ocupation():
    return render_template('cargo/update_ocupation.html')