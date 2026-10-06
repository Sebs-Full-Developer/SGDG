from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para los países
pais_bp = Blueprint('pais', __name__)

@pais_bp.route('/read_country')
def read_country():
    """Lee todos los registros de la tabla 'pais' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todos los países
        cursor.execute("{CALL proc_select_pais()}")
        paises = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not paises:
            paises = []

    except Exception as e:
        paises = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de los países
    return render_template('pais/read_country.html', paises=paises)

@pais_bp.route('/pais/create_country')
def create_country():
    return render_template('pais/create_country.html')

@pais_bp.route('/pais/delete_country')
def delete_country():
    return render_template('pais/delete_country.html')

@pais_bp.route('/pais/update_country')
def update_country():
    return render_template('pais/update_country.html')