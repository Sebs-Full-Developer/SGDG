class Genero:
    def __init__(self):
        self.id = None
        self.nombre_genero = None
        self.descripcion = None

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetNombreGenero(self, nombre_genero):
        self.nombre_genero = nombre_genero

    def GetNombreGenero(self):
        return self.nombre_genero

    def SetDescripcion(self, descripcion):
        self.descripcion = descripcion

    def GetDescripcion(self):
        return self.descripcion


class Usuario:
    def __init__(self):
        self.id = None
        self.username = None
        self.email = None

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetUsername(self, username):
        self.username = username

    def GetUsername(self):
        return self.username

    def SetEmail(self, email):
        self.email = email

    def GetEmail(self):
        return self.email


class Pais:
    def __init__(self):
        self.id = None
        self.nombre_pais = None
        self.descripcion = None

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetNombrePais(self, nombre_pais):
        self.nombre_pais = nombre_pais

    def GetNombrePais(self):
        return self.nombre_pais

    def SetDescripcion(self, descripcion):
        self.descripcion = descripcion

    def GetDescripcion(self):
        return self.descripcion


class Estado:
    def __init__(self):
        self.id = None
        self.nombre_estado = None
        self.descripcion = None

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetNombreEstado(self, nombre_estado):
        self.nombre_estado = nombre_estado

    def GetNombreEstado(self):
        return self.nombre_estado

    def SetDescripcion(self, descripcion):
        self.descripcion = descripcion

    def GetDescripcion(self):
        return self.descripcion


# Continúa con las demás clases: Ciudad, Persona, Telefono, Cargo, Entidad, AsignacionCargo

