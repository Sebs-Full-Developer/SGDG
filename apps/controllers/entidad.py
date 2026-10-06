from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para las entidades
entidad_bp = Blueprint('entidad', __name__)

@entidad_bp.route('/read_entity')
def read_entity():
    """Lee todos los registros de la tabla 'entidad' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todas las entidades
        cursor.execute("{CALL proc_select_entidad()}")
        entidades = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not entidades:
            entidades = []

    except Exception as e:
        entidades = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de las entidades
    return render_template('entidad/read_entity.html', entidades=entidades)

@entidad_bp.route('/entidad/create_entity')
def create_entity():
    return render_template('entidad/create_entity.html')

@entidad_bp.route('/entidad/delete_entity')
def delete_entity():
    return render_template('entidad/delete_entity.html')

@entidad_bp.route('/entidad/update_entity')
def update_entity():
    return render_template('entidad/update_entity.html')