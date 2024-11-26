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

    def delete_connection_genero(self, genero_id: int) -> bool:
            """
            Elimina un registro de la tabla genero según el ID proporcionado utilizando un procedimiento almacenado.

            Args:
                genero_id (int): El ID del registro a eliminar.

            Returns:
                bool: True si el registro fue eliminado correctamente, False de lo contrario.
            """
            conexion = pyodbc.connect(self.strConnection)
            cursor = conexion.cursor()

            try:
                # Llamar al procedimiento almacenado para eliminar el género
                cursor.execute("CALL proc_delete_genero(?)", (genero_id,))
                conexion.commit()  # Confirmar los cambios en la base de datos

                # Verificar si alguna fila fue afectada
                if cursor.rowcount > 0:
                    print(f"Género con ID {genero_id} eliminado correctamente.")
                    resultado = True
                else:
                    print(f"No se encontró ningún género con ID {genero_id}.")
                    resultado = False

            except Exception as e:
                print(f"Error al eliminar el género: {e}")
                resultado = False

            finally:
                cursor.close()
                conexion.close()

            return resultado
