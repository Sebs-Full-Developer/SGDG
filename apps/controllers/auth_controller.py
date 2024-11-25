import re
from flask import Blueprint, request, jsonify
from apps.services.database import create_connection
from apps.services.jwt_service import generate_token

auth_bp = Blueprint('auth', __name__)

def is_safe_username(username):
    """ Valida que el username no contenga caracteres peligrosos para evitar inyecciones SQL """
    # Solo permitimos caracteres alfanuméricos y un guion bajo para el username
    return bool(re.match("^[a-zA-Z0-9_]+$", username))

@auth_bp.route('/login', methods=['POST'])
def login():
    """ Ruta para realizar login y obtener un token """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validamos que se reciban ambos parámetros
    if not username or not password:
        return jsonify({"message": "Faltan parámetros: username o password"}), 400

    # Validamos el username para evitar inyección SQL
    if not is_safe_username(username):
        return jsonify({"message": "El nombre de usuario contiene caracteres no permitidos."}), 400

    # Conexión a la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    # Usamos f-string, pero ya validado el username
    query = f"SELECT * FROM usuario WHERE username = '{username}'"

    # Ejecutamos la consulta para obtener el usuario
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    # Si el usuario no existe, retornamos un error
    if not user:
        return jsonify({"message": "Credenciales inválidas"}), 401

    # Desempaquetamos los valores del usuario obtenido
    user_id, stored_username, stored_password, email, fecha_creacion = user

    # Verificamos que la contraseña coincida con la almacenada (texto plano)
    if stored_password == password:
        # Generamos el token y lo almacenamos en la base de datos
        token = generate_token(username)  # Generamos el token y lo almacenamos
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401