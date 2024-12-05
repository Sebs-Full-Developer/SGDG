from flask import Blueprint, render_template
from apps.services.database import create_connection  # Conexión a la base de datos

# Crear un blueprint para el usuario
usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/read_user')
def read_user():
    """Lee todos los registros de la tabla 'usuario' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todos los usuarios
        cursor.execute("{CALL proc_select_usuario()}")
        users = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not users:
            users = []

    except Exception as e:
        users = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de los usuarios
    return render_template('usuario/read_user.html', users=users)

@usuario_bp.route('/usuario/create_user')
def create_user():
    return render_template('usuario/create_user.html')

@usuario_bp.route('/usuario/delete_user')
def delete_user():
    return render_template('usuario/delete_user.html')

@usuario_bp.route('/usuario/update_user')
def update_user():
    return render_template('usuario/update_user.html')