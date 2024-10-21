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

    # Método para eliminar género
    def delete_genero(self, genero_id) -> None:
        if not genero_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `genero` WHERE `genero`.`genero_id` = {genero_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Género eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el género: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar usuario
    def delete_usuario(self, usuario_id) -> None:
        if not usuario_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `usuario` WHERE `usuario`.`usuario_id` = {usuario_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Usuario eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar país
    def delete_pais(self, pais_id) -> None:
        if not pais_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `pais` WHERE `pais`.`pais_id` = {pais_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("País eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el país: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar estado
    def delete_estado(self, estado_id) -> None:
        if not estado_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `estado` WHERE `estado`.`estado_id` = {estado_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Estado eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el estado: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar ciudad
    def delete_ciudad(self, ciudad_id) -> None:
        if not ciudad_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `ciudad` WHERE `ciudad`.`ciudad_id` = {ciudad_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Ciudad eliminada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar la ciudad: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar persona
    def delete_persona(self, persona_id) -> None:
        if not persona_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `persona` WHERE `persona`.`persona_id` = {persona_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Persona eliminada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar la persona: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar teléfono
    def delete_telefono(self, telefono_id) -> None:
        if not telefono_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `telefono` WHERE `telefono`.`telefono_id` = {telefono_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Teléfono eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el teléfono: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar cargo
    def delete_cargo(self, cargo_id) -> None:
        if not cargo_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `cargo` WHERE `cargo`.`cargo_id` = {cargo_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Cargo eliminado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el cargo: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar entidad
    def delete_entidad(self, entidad_id) -> None:
        if not entidad_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `entidad` WHERE `entidad`.`entidad_id` = {entidad_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Entidad eliminada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar la entidad: {e}")
        finally:
            cursor.close()
            conexion.close()

    # Método para eliminar asignación de cargo
    def delete_asignacion_cargo(self, asignacion_id) -> None:
        if not asignacion_id:
            print("Error: ID no puede estar vacío.")
            return

        conexion = pyodbc.connect(self.strConnection)
        consulta = f"DELETE FROM `asignacion_cargo` WHERE `asignacion_cargo`.`asignacion_id` = {asignacion_id}"

        try:
            cursor = conexion.cursor()
            cursor.execute(consulta)
            conexion.commit()
            print("Asignación de cargo eliminada correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar la asignación de cargo: {e}")
        finally:
            cursor.close()
            conexion.close()