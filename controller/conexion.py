import pyodbc
from controller.clases import Genero

class Conexion:
    strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_gobierno;
        PORT=3306;
        user=root;
        """

    def list_connection_genero(self) -> list:
        """
        Obtiene una lista de todos los géneros en la base de datos.

        Returns:
            list: Lista de objetos Genero.
        """
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        cursor.execute("SELECT genero_id, nombre_genero, descripcion FROM genero")
        lista = []
        
        for elemento in cursor:
            entidad = Genero()
            entidad.SetId(elemento[0])
            entidad.SetNombreGenero(elemento[1])
            entidad.SetDescripcion(elemento[2])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()
        
        return lista

    def create_connection_genero(self, nombre_genero: str, descripcion: str) -> bool:
        """
        Crea un nuevo registro en la tabla genero.

        Args:
            nombre_genero (str): El nombre del género.
            descripcion (str): La descripción del género.

        Returns:
            bool: True si el registro fue creado correctamente, False de lo contrario.
        """
        print(f"Intentando crear género con nombre: {nombre_genero}, descripción: {descripcion}")
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        try:
            query = f"INSERT INTO genero (nombre_genero, descripcion) VALUES ('{nombre_genero}', '{descripcion}')"
            print(f"Ejecutando consulta directa: {query}")
            cursor.execute(query)
            conexion.commit()
            print("Género creado correctamente.")
            return True

        except Exception as e:
            print(f"Error al crear el género: {e}")
            return False

        finally:
            cursor.close()
            conexion.close()


    def update_connection_genero(self, genero_id: int, nombre_genero: str, descripcion: str) -> bool:
        """
        Actualiza un registro en la tabla genero utilizando una consulta SQL formateada.

        Args:
            genero_id (int): El ID del género a actualizar.
            nombre_genero (str): El nuevo nombre del género.
            descripcion (str): La nueva descripción del género.

        Returns:
            bool: True si el registro fue actualizado correctamente, False de lo contrario.
        """
        print(f"Intentando actualizar género con ID: {genero_id}, nombre: {nombre_genero}, descripción: {descripcion}")
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        try:
            # Consulta SQL formateada
            query = f"""
            UPDATE genero
            SET nombre_genero = '{nombre_genero}', descripcion = '{descripcion}'
            WHERE genero_id = {genero_id}
            """
            print(f"Ejecutando consulta: {query}")
            cursor.execute(query)
            conexion.commit()

            # Verificar si alguna fila fue afectada
            if cursor.rowcount > 0:
                print(f"Género con ID {genero_id} actualizado correctamente.")
                return True
            else:
                print(f"No se encontró ningún género con ID {genero_id}.")
                return False

        except Exception as e:
            print(f"Error al actualizar el género: {e}")
            return False

        finally:
            cursor.close()
            conexion.close()

    def delete_connection_genero(self, genero_id: int) -> bool:
        """
        Elimina un registro de la tabla genero según el ID proporcionado.

        Args:
            genero_id (int): El ID del registro a eliminar.

        Returns:
            bool: True si el registro fue eliminado correctamente, False de lo contrario.
        """
        print(f"Intentando eliminar el género con ID: {genero_id}")
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        genero_id = int(genero_id)

        try:
            query = f"DELETE FROM genero WHERE genero_id = {genero_id}"
            print(f"Ejecutando consulta: {query}")
            cursor.execute(query)
            conexion.commit()

            if cursor.rowcount > 0:
                print(f"Género con ID {genero_id} eliminado correctamente.")
                return True
            else:
                print(f"No se encontró ningún género con ID {genero_id}.")
                return False

        except Exception as e:
            print(f"Error al eliminar el género: {e}")
            return False

        finally:
            cursor.close()
            conexion.close()
