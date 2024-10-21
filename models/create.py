import pyodbc
from controller.clases import *

class Conexion:
    strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_gobierno;
        PORT=3306;
        user=user_software_libre;
        password=Access123456*"""

    # Método para insertar género
    def create_genero(self, nombre_genero, descripcion) -> None:
        if not nombre_genero or not descripcion:
            print("Error: Nombre género y descripción no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO genero (nombre_genero, descripcion) VALUES ('{nombre_genero}', '{descripcion}')"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Género insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar el género: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar usuario
    def create_usuario(self, username, password_hash, email) -> None:
        if not username or not password_hash or not email:
            print("Error: Username, password hash y email no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO usuario (username, password_hash, email) VALUES ('{username}', '{password_hash}', '{email}')"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Usuario insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar país
    def create_pais(self, nombre_pais, descripcion) -> None:
        if not nombre_pais or not descripcion:
            print("Error: Nombre país y descripción no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO pais (nombre_pais, descripcion) VALUES ('{nombre_pais}', '{descripcion}')"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("País insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar el país: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar estado
    def create_estado(self, nombre_estado, descripcion, pais_id) -> None:
        if not nombre_estado or not descripcion or not pais_id:
            print("Error: Nombre estado, descripción y país ID no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO estado (nombre_estado, descripcion, pais_id) VALUES ('{nombre_estado}', '{descripcion}', {pais_id})"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Estado insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar el estado: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar ciudad
    def create_ciudad(self, nombre_ciudad, descripcion, estado_id) -> None:
        if not nombre_ciudad or not descripcion or not estado_id:
            print("Error: Nombre ciudad, descripción y estado ID no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO ciudad (nombre_ciudad, descripcion, estado_id) VALUES ('{nombre_ciudad}', '{descripcion}', {estado_id})"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Ciudad insertada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar la ciudad: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar persona
    def create_persona(self, nombre_persona, apellido_persona, documento_identidad, genero_id, ciudad_id) -> None:
        if not nombre_persona or not apellido_persona or not documento_identidad or not genero_id or not ciudad_id:
            print("Error: Todos los campos son obligatorios.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO persona (nombre_persona, apellido_persona, documento_identidad, genero_id, ciudad_id) VALUES ('{nombre_persona}', '{apellido_persona}', '{documento_identidad}', {genero_id}, {ciudad_id})"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Persona insertada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar la persona: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar teléfono
    def create_telefono(self, tipo_telefono, numero_telefono, persona_id) -> None:
        if not tipo_telefono or not numero_telefono or not persona_id:
            print("Error: Número de teléfono y persona ID no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO telefono (tipo_telefono, numero_telefono, persona_id) VALUES ('{tipo_telefono}', '{numero_telefono}', {persona_id})"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Teléfono insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar el teléfono: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar cargo
    def create_cargo(self, titulo, descripcion) -> None:
        if not titulo or not descripcion:
            print("Error: Título y descripción no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO cargo (titulo, descripcion) VALUES ('{titulo}', '{descripcion}')"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Cargo insertado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar el cargo: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar entidad
    def create_entidad(self, nombre_entidad, descripcion, tipo_entidad) -> None:
        if not nombre_entidad or not descripcion or not tipo_entidad:
            print("Error: Nombre entidad, descripción y tipo de entidad no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO entidad (nombre_entidad, descripcion, tipo_entidad) VALUES ('{nombre_entidad}', '{descripcion}', '{tipo_entidad}')"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Entidad insertada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar la entidad: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para insertar asignación de cargo
    def create_asignacion_cargo(self, persona_id, cargo_id, entidad_id, fecha_inicio, fecha_fin, estado) -> None:
        if not persona_id or not cargo_id or not entidad_id or not fecha_inicio:
            print("Error: Persona ID, cargo ID, entidad ID y fecha de inicio son obligatorios.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"INSERT INTO asignacion_cargo (persona_id, cargo_id, entidad_id, fecha_inicio, fecha_fin, estado) VALUES ({persona_id}, {cargo_id}, {entidad_id}, '{fecha_inicio}', '{fecha_fin}', '{estado}')"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Asignación de cargo insertada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar la asignación de cargo: {e}")
        finally:
            cursor.close()
            conexion.close()
