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

    # Método para actualizar género
    def update_genero(self, genero_id, nuevo_nombre, nueva_descripcion) -> None:
        if not genero_id or not nuevo_nombre or not nueva_descripcion:
            print("Error: ID, nombre y descripción no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `genero` SET `nombre_genero` = '{nuevo_nombre}', `descripcion` = '{nueva_descripcion}' WHERE `genero`.`genero_id` = {genero_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Género actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el género: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar usuario
    def update_usuario(self, usuario_id, nuevo_username, nuevo_password_hash, nuevo_email) -> None:
        if not usuario_id or not nuevo_username or not nuevo_password_hash or not nuevo_email:
            print("Error: ID, nombre de usuario, hash de contraseña y email no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `usuario` SET `username` = '{nuevo_username}', `password_hash` = '{nuevo_password_hash}', `email` = '{nuevo_email}' WHERE `usuario`.`usuario_id` = {usuario_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Usuario actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar país
    def update_pais(self, pais_id, nuevo_nombre, nueva_descripcion) -> None:
        if not pais_id or not nuevo_nombre or not nueva_descripcion:
            print("Error: ID, nombre y descripción no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `pais` SET `nombre_pais` = '{nuevo_nombre}', `descripcion` = '{nueva_descripcion}' WHERE `pais`.`pais_id` = {pais_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("País actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el país: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar estado
    def update_estado(self, estado_id, nuevo_nombre, nueva_descripcion, nuevo_pais_id) -> None:
        if not estado_id or not nuevo_nombre or not nueva_descripcion or not nuevo_pais_id:
            print("Error: ID, nombre, descripción y ID de país no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `estado` SET `nombre_estado` = '{nuevo_nombre}', `descripcion` = '{nueva_descripcion}', `pais_id` = {nuevo_pais_id} WHERE `estado`.`estado_id` = {estado_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Estado actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el estado: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar ciudad
    def update_ciudad(self, ciudad_id, nuevo_nombre, nueva_descripcion, nuevo_estado_id) -> None:
        if not ciudad_id or not nuevo_nombre or not nueva_descripcion or not nuevo_estado_id:
            print("Error: ID, nombre, descripción y ID de estado no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `ciudad` SET `nombre_ciudad` = '{nuevo_nombre}', `descripcion` = '{nueva_descripcion}', `estado_id` = {nuevo_estado_id} WHERE `ciudad`.`ciudad_id` = {ciudad_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Ciudad actualizada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar la ciudad: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar persona
    def update_persona(self, persona_id, nuevo_nombre, nuevo_apellido, nuevo_documento_identidad, nuevo_genero_id, nuevo_ciudad_id) -> None:
        if not persona_id or not nuevo_nombre or not nuevo_apellido or not nuevo_documento_identidad or not nuevo_genero_id or not nuevo_ciudad_id:
            print("Error: ID, nombre, apellido, documento de identidad, ID de género y ID de ciudad no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `persona` SET `nombre_persona` = '{nuevo_nombre}', `apellido_persona` = '{nuevo_apellido}', `documento_identidad` = '{nuevo_documento_identidad}', `genero_id` = {nuevo_genero_id}, `ciudad_id` = {nuevo_ciudad_id} WHERE `persona`.`persona_id` = {persona_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Persona actualizada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar la persona: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar teléfono
    def update_telefono(self, telefono_id, nuevo_tipo_telefono, nuevo_numero_telefono) -> None:
        if not telefono_id or not nuevo_tipo_telefono or not nuevo_numero_telefono:
            print("Error: ID, tipo de teléfono y número de teléfono no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `telefono` SET `tipo_telefono` = '{nuevo_tipo_telefono}', `numero_telefono` = '{nuevo_numero_telefono}' WHERE `telefono`.`telefono_id` = {telefono_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Teléfono actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el teléfono: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar cargo
    def update_cargo(self, cargo_id, nuevo_titulo, nueva_descripcion) -> None:
        if not cargo_id or not nuevo_titulo or not nueva_descripcion:
            print("Error: ID, título y descripción no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `cargo` SET `titulo` = '{nuevo_titulo}', `descripcion` = '{nueva_descripcion}' WHERE `cargo`.`cargo_id` = {cargo_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Cargo actualizado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar el cargo: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar entidad
    def update_entidad(self, entidad_id, nuevo_nombre, nueva_descripcion, nuevo_tipo_entidad) -> None:
        if not entidad_id or not nuevo_nombre or not nueva_descripcion or not nuevo_tipo_entidad:
            print("Error: ID, nombre, descripción y tipo de entidad no pueden estar vacíos.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `entidad` SET `nombre_entidad` = '{nuevo_nombre}', `descripcion` = '{nueva_descripcion}', `tipo_entidad` = '{nuevo_tipo_entidad}' WHERE `entidad`.`entidad_id` = {entidad_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Entidad actualizada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar la entidad: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para actualizar asignación de cargo
    def update_asignacion_cargo(self, asignacion_id, nuevo_persona_id, nuevo_cargo_id, nuevo_entidad_id, nueva_fecha_inicio, nueva_fecha_fin, nuevo_estado) -> None:
        if not asignacion_id or not nuevo_persona_id or not nuevo_cargo_id or not nuevo_entidad_id or not nueva_fecha_inicio:
            print("Error: ID, persona ID, cargo ID, entidad ID y fecha de inicio son obligatorios.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"UPDATE `asignacion_cargo` SET `persona_id` = {nuevo_persona_id}, `cargo_id` = {nuevo_cargo_id}, `entidad_id` = {nuevo_entidad_id}, `fecha_inicio` = '{nueva_fecha_inicio}', `fecha_fin` = '{nueva_fecha_fin}', `estado` = '{nuevo_estado}' WHERE `asignacion_cargo`.`asignacion_id` = {asignacion_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Asignación de cargo actualizada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al actualizar la asignación de cargo: {e}")
        finally:
            cursor.close()
            conexion.close()
