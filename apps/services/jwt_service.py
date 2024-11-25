# services/jwt_service.py
import jwt
import datetime
from apps.services.database import create_connection

SECRET_KEY = "9d05X8ORk2jR8lLCy832rWLzqMjTIgMKlch3FEhH0Mc0osGwtyvh72vooTWWMrxM"  # Asegúrate de que sea una clave secreta fuerte

def generate_token(username):
    """ Genera un token JWT para el usuario y lo guarda en la base de datos """
    # Usamos un objeto consciente de la zona horaria en UTC
    expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    
    payload = {
        'username': username,
        'exp': expiration_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    # Almacenamos el token en la base de datos
    conn = create_connection()
    cursor = conn.cursor()

    '''[ ============================================================================================]
    # Primero, intentamos borrar el token anterior (si existía) antes de insertar el nuevo
    cursor.execute("DELETE FROM clave WHERE username=%s", (username,))
    
    # Insertamos el nuevo token en la tabla clave
    cursor.execute("INSERT INTO clave (username, token) VALUES (%s, %s)", (username, token))
    conn.commit()  # Confirmamos la transacción
    conn.close()
    [ ============================================================================================]'''

    # Construimos la consulta para borrar el token anterior utilizando f-string
    query_delete = f"DELETE FROM clave WHERE username = '{username}'"
    cursor.execute(query_delete)

    # Construimos la consulta para insertar el nuevo token utilizando f-string
    query_insert = f"INSERT INTO clave (username, token) VALUES ('{username}', '{token}')"

    # Ejecutamos la inserción del nuevo token
    cursor.execute(query_insert)
    conn.commit()  # Confirmamos la transacción
    conn.close()

    return token

def verify_token(token):
    """ Verifica un token JWT y devuelve los datos del payload """
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded  # Retorna los datos decodificados del token
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido
