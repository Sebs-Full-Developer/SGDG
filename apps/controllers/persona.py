from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para las personas
persona_bp = Blueprint('persona', __name__)

@persona_bp.route('/read_person')
def read_person():
    """Lee todos los registros de la tabla 'persona' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todas las personas
        cursor.execute("{CALL proc_select_persona()}")
        personas = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not personas:
            personas = []

    except Exception as e:
        personas = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de las personas
    return render_template('persona/read_person.html', personas=personas)

@persona_bp.route('/persona/create_person')
def create_person():
    return render_template('persona/create_person.html')

@persona_bp.route('/persona/delete_person')
def delete_person():
    return render_template('persona/delete_person.html')

@persona_bp.route('/persona/update_person')
def update_person():
    return render_template('persona/update_person.html')