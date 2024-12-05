# services/database.py
import pyodbc

def create_connection():
    """ Crea una conexión a la base de datos MySQL usando ODBC """
    conn_str = (
        "Driver={MySQL ODBC 9.0 Unicode Driver};"
        "Server=localhost;"
        "Database=db_gobierno;"
        "PORT=3306;"
        "user=user_software_libre;"
        "password=Access123456*;"
    )

    try:
        # Intentamos crear la conexión con los detalles proporcionados
        connection = pyodbc.connect(conn_str)
        print("Conexión exitosa a la base de datos")
        return connection
    except pyodbc.Error as e:
        # Si ocurre un error, lo manejamos aquí
        print(f"Error de conexión: {e}")
        return None
