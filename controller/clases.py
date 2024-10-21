import pyodbc;
import datetime;
import decimal;

class Genero:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre_genero: str = None
    def GetNombreGenero(self) -> str:
        return self.nombre_genero
    def SetNombreGenero(self, value: str) -> None:
        self.nombre_genero = value

    descripcion: str = None
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

class Usuario:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    username: str = None
    def GetUsername(self) -> str:
        return self.username
    def SetUsername(self, value: str) -> None:
        self.username = value

    password_hash: str = None
    def GetPasswordHash(self) -> str:
        return self.password_hash
    def SetPasswordHash(self, value: str) -> None:
        self.password_hash = value

    email: str = None
    def GetEmail(self) -> str:
        return self.email
    def SetEmail(self, value: str) -> None:
        self.email = value

class Pais:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre_pais: str = 'Colombia'
    def GetNombrePais(self) -> str:
        return self.nombre_pais
    def SetNombrePais(self, value: str) -> None:
        self.nombre_pais = value

    descripcion: str = None
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

class Estado:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre_estado: str = None
    def GetNombreEstado(self) -> str:
        return self.nombre_estado
    def SetNombreEstado(self, value: str) -> None:
        self.nombre_estado = value

    descripcion: str = None
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    _pais: Pais = None
    def GetPais(self) -> Pais:
        return self._pais
    def SetPais(self, value: Pais) -> None:
        self._pais = value

class Ciudad:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre_ciudad: str = None
    def GetNombreCiudad(self) -> str:
        return self.nombre_ciudad
    def SetNombreCiudad(self, value: str) -> None:
        self.nombre_ciudad = value

    descripcion: str = None
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    _estado: Estado = None
    def GetEstado(self) -> Estado:
        return self._estado
    def SetEstado(self, value: Estado) -> None:
        self._estado = value

class Persona:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre_persona: str = None
    def GetNombrePersona(self) -> str:
        return self.nombre_persona
    def SetNombrePersona(self, value: str) -> None:
        self.nombre_persona = value

    apellido_persona: str = None
    def GetApellidoPersona(self) -> str:
        return self.apellido_persona
    def SetApellidoPersona(self, value: str) -> None:
        self.apellido_persona = value

    documento_identidad: str = None
    def GetDocumentoIdentidad(self) -> str:
        return self.documento_identidad
    def SetDocumentoIdentidad(self, value: str) -> None:
        self.documento_identidad = value

    _genero: Genero = None
    def GetGenero(self) -> Genero:
        return self._genero
    def SetGenero(self, value: Genero) -> None:
        self._genero = value

    _ciudad: Ciudad = None
    def GetCiudad(self) -> Ciudad:
        return self._ciudad
    def SetCiudad(self, value: Ciudad) -> None:
        self._ciudad = value

class Telefono:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    tipo_telefono: str = None
    def GetTipoTelefono(self) -> str:
        return self.tipo_telefono
    def SetTipoTelefono(self, value: str) -> None:
        self.tipo_telefono = value

    numero_telefono: str = None
    def GetNumeroTelefono(self) -> str:
        return self.numero_telefono
    def SetNumeroTelefono(self, value: str) -> None:
        self.numero_telefono = value

    _persona: Persona = None
    def GetPersona(self) -> Persona:
        return self._persona
    def SetPersona(self, value: Persona) -> None:
        self._persona = value

class Cargo:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    titulo: str = None
    def GetTitulo(self) -> str:
        return self.titulo
    def SetTitulo(self, value: str) -> None:
        self.titulo = value

    descripcion: str = None
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

class Entidad:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre_entidad: str = None
    def GetNombreEntidad(self) -> str:
        return self.nombre_entidad
    def SetNombreEntidad(self, value: str) -> None:
        self.nombre_entidad = value

    descripcion: str = None
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    tipo_entidad: str = None
    def GetTipoEntidad(self) -> str:
        return self.tipo_entidad
    def SetTipoEntidad(self, value: str) -> None:
        self.tipo_entidad = value

class AsignacionCargo:
    id: int = 0
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    _persona: Persona = None
    def GetPersona(self) -> Persona:
        return self._persona
    def SetPersona(self, value: Persona) -> None:
        self._persona = value

    _cargo: Cargo = None
    def GetCargo(self) -> Cargo:
        return self._cargo
    def SetCargo(self, value: Cargo) -> None:
        self._cargo = value

    _entidad: Entidad = None
    def GetEntidad(self) -> Entidad:
        return self._entidad
    def SetEntidad(self, value: Entidad) -> None:
        self._entidad = value

    fecha_inicio: str = None
    def GetFechaInicio(self) -> str:
        return self.fecha_inicio
    def SetFechaInicio(self, value: str) -> None:
        self.fecha_inicio = value

    fecha_fin: str = None
    def GetFechaFin(self) -> str:
        return self.fecha_fin
    def SetFechaFin(self, value: str) -> None:
        self.fecha_fin = value

    estado: str = 'Activo'
    def GetEstado(self) -> str:
        return self.estado
    def SetEstado(self, value: str) -> None:
        self.estado = value