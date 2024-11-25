from flask import Blueprint, render_template, request, redirect, url_for, flash
import pyodbc
from apps.services.database import create_connection  # Asegúrate de tener esta función de conexión

# Crear un blueprint para el home
genero_bp = Blueprint('genero', __name__)

@genero_bp.route('/read_gender')
def read_gender():
    """Lee todos los registros de la tabla 'genero' usando el procedimiento almacenado"""
    
    # Conectar a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Llamar al procedimiento almacenado para seleccionar todos los géneros
        cursor.execute("{CALL proc_select_genero()}")
        genres = cursor.fetchall()  # Obtener todos los resultados

        # Si no hay datos, se puede enviar un mensaje o una lista vacía
        if not genres:
            genres = []

    except Exception as e:
        genres = []
        print(f"Error al ejecutar el procedimiento: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

    # Renderizar la plantilla y pasar los datos de los géneros
    return render_template('genero/read_gender.html', genres=genres)

@genero_bp.route('/genero/create_gender', methods=['GET', 'POST'])
def create_gender():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_genero = request.form['nombre_genero']
        descripcion = request.form['descripcion']

        # Llamar al procedimiento almacenado para insertar el nuevo género
        conn = create_connection()
        cursor = conn.cursor()

        try:
            # Llamar al procedimiento almacenado para insertar el nuevo género
            # Usando una cadena f para crear la consulta
            query = f"CALL proc_insert_genero('{nombre_genero}', '{descripcion}')"
            cursor.execute(query)

            conn.commit()  # Asegúrate de confirmar la transacción
            return redirect(url_for('genero.read_gender'))  # Redirigir al listado de géneros

        except Exception as e:
            print(f"Error al ejecutar el procedimiento: {e}")
            return render_template('genero/create_gender.html', error="Hubo un problema al crear el género.")

        finally:
            conn.close()

    # Si es GET, simplemente mostrar el formulario
    return render_template('genero/create_gender.html')

@genero_bp.route('/genero/delete_gender')
def delete_gender():
    return render_template('genero/delete_gender.html')

@genero_bp.route('/genero/update_gender/<int:genero_id>', methods=['GET', 'POST'])
def update_gender(genero_id):
    """Actualiza un género existente en la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()

    # Si el formulario es enviado (método POST)
    if request.method == 'POST':
        nombre_genero = request.form['nombre_genero']
        descripcion = request.form['descripcion']

        try:
            # Crear la consulta SQL con f-string (aunque no es lo más seguro)
            query = f"CALL proc_update_genero({genero_id}, '{nombre_genero}', '{descripcion}')"
            cursor.execute(query)
            conn.commit()  # Confirmar cambios

            flash("Género actualizado correctamente", "success")

            return redirect(url_for('genero.read_gender'))  # Redirigir a la vista de géneros

        except Exception as e:
            flash(f"Error al actualizar el género: {e}", "danger")
            return redirect(url_for('genero.read_gender'))

    # Si es un GET, se cargan los datos del género para mostrarlos en el formulario
    try:
        cursor.execute(f"SELECT * FROM genero WHERE genero_id = {genero_id}")
        genero = cursor.fetchone()

        if not genero:
            flash("Género no encontrado", "danger")
            return redirect(url_for('genero.read_gender'))

    except Exception as e:
        flash(f"Error al cargar el género: {e}", "danger")
        return redirect(url_for('genero.read_gender'))

    finally:
        conn.close()

    return redirect(url_for('genero.update_gender', genero_id=genero_id))
