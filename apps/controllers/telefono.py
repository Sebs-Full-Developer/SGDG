from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para los teléfonos
telefono_bp = Blueprint('telefono', __name__)

@telefono_bp.route('/read_cellphone')
def read_cellphone():
    """Lee todos los registros de la tabla 'telefono' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todos los teléfonos
        cursor.execute("{CALL proc_select_telefono()}")
        telefonos = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not telefonos:
            telefonos = []

    except Exception as e:
        telefonos = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de los teléfonos
    return render_template('telefono/read_cellphone.html', telefonos=telefonos)

@telefono_bp.route('/telefono/create_cellphone')
def create_cellphone():
    return render_template('telefono/create_cellphone.html')

@telefono_bp.route('/telefono/delete_cellphone')
def delete_cellphone():
    return render_template('telefono/delete_cellphone.html')

@telefono_bp.route('/telefono/update_cellphone')
def update_cellphone():
    return render_template('telefono/update_cellphone.html')