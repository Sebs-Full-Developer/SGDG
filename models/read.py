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

    def list_connection_genero(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_genero()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Genero()
            entidad.SetId(elemento[0])
            entidad.SetNombreGenero(elemento[1])
            entidad.SetDescripcion(elemento[2])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Género: {dato.GetNombreGenero()}, Descripción: {dato.GetDescripcion()}")

    def list_connection_usuario(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_usuario()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Usuario()
            entidad.SetId(elemento[0])
            entidad.SetUsername(elemento[1])
            entidad.SetPasswordHash(elemento[2])
            entidad.SetEmail(elemento[3])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Username: {dato.GetUsername()}, Email: {dato.GetEmail()}")

    def list_connection_pais(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_pais()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Pais()
            entidad.SetId(elemento[0])
            entidad.SetNombrePais(elemento[1])
            entidad.SetDescripcion(elemento[2])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre País: {dato.GetNombrePais()}, Descripción: {dato.GetDescripcion()}")

    def list_connection_estado(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_estado()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Estado()
            entidad.SetId(elemento[0])
            entidad.SetNombreEstado(elemento[1])
            entidad.SetDescripcion(elemento[2])
            entidad.SetPais(Pais())
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Estado: {dato.GetNombreEstado()}, Descripción: {dato.GetDescripcion()}")

    def list_connection_ciudad(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_ciudad()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Ciudad()
            entidad.SetId(elemento[0])
            entidad.SetNombreCiudad(elemento[1])
            entidad.SetDescripcion(elemento[2])
            entidad.SetEstado(Estado())
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Ciudad: {dato.GetNombreCiudad()}, Descripción: {dato.GetDescripcion()}")

    def list_connection_persona(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_persona()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Persona()
            entidad.SetId(elemento[0])
            entidad.SetNombrePersona(elemento[1])
            entidad.SetApellidoPersona(elemento[2])
            entidad.SetDocumentoIdentidad(elemento[3])
            entidad.SetGenero(Genero())
            entidad.SetCiudad(Ciudad())
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre: {dato.GetNombrePersona()}, Apellido: {dato.GetApellidoPersona()}")

    def list_connection_telefono(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_telefono()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Telefono()
            entidad.SetId(elemento[0])
            entidad.SetTipoTelefono(elemento[1])
            entidad.SetNumeroTelefono(elemento[2])
            entidad.SetPersona(Persona())
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Tipo Teléfono: {dato.GetTipoTelefono()}, Número: {dato.GetNumeroTelefono()}")

    def list_connection_cargo(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_cargo()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Cargo()
            entidad.SetId(elemento[0])
            entidad.SetTitulo(elemento[1])
            entidad.SetDescripcion(elemento[2])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Título: {dato.GetTitulo()}, Descripción: {dato.GetDescripcion()}")

    def list_connection_entidad(self) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute("CALL proc_select_entidad()")  # Llama al procedimiento almacenado
        lista: list = []
        
        for elemento in cursor:
            entidad = Entidad()
            entidad.SetId(elemento[0])
            entidad.SetNombreEntidad(elemento[1])
            entidad.SetDescripcion(elemento[2])
            entidad.SetTipoEntidad(elemento[3])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Entidad: {dato.GetNombreEntidad()}, Descripción: {dato.GetDescripcion()}")

    def list_connection_asignacion_cargo(self) -> None:
        # Implementar similar a los otros métodos
        pass

        conexion = pyodbc.connect(self.strConnection)
        consulta: str = """SELECT * FROM asignacion_cargo"""
        
        cursor = conexion.cursor()
        cursor.execute(consulta)
        lista: list = []
        
        for elemento in cursor:
            entidad = AsignacionCargo()
            entidad.SetId(elemento[0])
            entidad.SetPersona(Persona())
            entidad.SetCargo(Cargo()) 
            entidad.SetEntidad(Entidad())
            entidad.SetFechaInicio(elemento[4])
            entidad.SetFechaFin(elemento[5])
            entidad.SetEstado(elemento[6])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Estado: {dato.GetEstado()}, Fecha Inicio: {dato.GetFechaInicio()}, Fecha Fin: {dato.GetFechaFin()}")
