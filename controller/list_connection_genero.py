def list_connection_genero(self) -> list:
    conexion = pyodbc.connect(self.strConnection)
    cursor = conexion.cursor()
    
    cursor.execute("CALL proc_select_genero()")
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
