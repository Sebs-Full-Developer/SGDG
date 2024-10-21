import time
from controller.clases import *
import speed_text as impt

import models.create as crear
import models.read as leer
import models.update as actualizar
import models.delete as borrar

class Iniciar:
    def __init__(self) -> None:
        impt.imprimir_letra_por_letra("\n==============================\n\nProceso de SGDG Iniciado. \nConexión iniciada ....\nDatos de conexión recibidos.\n\n==============================\n\n", delay=0.01)
        time.sleep(3);
        self.ejecutar_accion()

    def ejecutar_accion(self):
        while True:
            self.accion = int(impt.input_animado(
                "Bienvenido al Sistema de Gestión Documental del Gobierno de la Republica de Colombia (SGDG)\n\n"
                "Este sistema te permite gestionar personas en cargos públicos del gobierno, para así llevar un debido registro y control,\n"
                "por favor digite el número el cual representa la acción a ejecutar:\n\n"
                "   1 = Crear un registro.\n"
                "   2 = Leer los registros.\n"
                "   3 = Actualizar los registros.\n"
                "   4 = Eliminar un registro.\n"
                "   5 = Terminar.\n\n"
                "Insertar número...\n   "
            , delay=0.03))
            impt.imprimir_letra_por_letra("\n==============================\n\n")

            if self.accion == 1:
                self.crear_registro()
            elif self.accion == 2:
                self.leer_registros()
            elif self.accion == 3:
                self.actualizar_registro()
            elif self.accion == 4:
                self.eliminar_registro()
            elif self.accion == 5:
                impt.imprimir_letra_por_letra("\nTerminando el programa, feliz resto de día ... \nAdios")
                break
            else:
                impt.imprimir_letra_por_letra("Acción no válida, por favor recuerde ingresar solo números entre el 1 y el 5.\n Por favor, intente de nuevo.")
            
            # Preguntar si desea hacer otra acción
            continuar = impt.input_animado("¿Desea realizar otra acción? (s/n): ", delay=0.01).strip().lower()
            if continuar != 's':
                impt.imprimir_letra_por_letra("\nTerminando el programa, feliz resto de día ... \nAdios")
                break

    def crear_registro(self):
        tipo_registro = int(impt.input_animado(
            "Seleccione el tipo de registro que desea crear:\n"
            "   1 = Género\n"
            "   2 = Usuario\n"
            "   3 = País\n"
            "   4 = Estado\n"
            "   5 = Ciudad\n"
            "   6 = Persona\n"
            "   7 = Teléfono\n"
            "   8 = Cargo\n"
            "   9 = Entidad\n"
            "   10 = Asignación de Cargo\n"
            "Inserte el número de opción...\n   ", delay=0.03))

        if tipo_registro == 1:
            nombre = impt.input_animado("Ingrese el nombre del género: ", delay=0.01)
            descripcion = impt.input_animado("Ingrese la descripción del género: ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_genero(nombre, descripcion)
        elif tipo_registro == 2:
            username = impt.input_animado("Ingrese el nombre de usuario: ", delay=0.01)
            password_hash = impt.input_animado("Ingrese el hash de la contraseña: ", delay=0.01)
            email = impt.input_animado("Ingrese el email: ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_usuario(username, password_hash, email)
        elif tipo_registro == 3:
            nombre = impt.input_animado("Ingrese el nombre del país: ", delay=0.01)
            descripcion = impt.input_animado("Ingrese la descripción del país: ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_pais(nombre, descripcion)
        elif tipo_registro == 4:
            nombre = impt.input_animado("Ingrese el nombre del estado: ", delay=0.01)
            descripcion = impt.input_animado("Ingrese la descripción del estado: ", delay=0.01)
            pais_id = impt.input_animado("Ingrese el ID del país (ejemplo: 1 para Colombia): ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_estado(nombre, descripcion, pais_id)
        elif tipo_registro == 5:
            nombre = impt.input_animado("Ingrese el nombre de la ciudad: ", delay=0.01)
            descripcion = impt.input_animado("Ingrese la descripción de la ciudad: ", delay=0.01)
            estado_id = impt.input_animado("Ingrese el ID del estado (ejemplo: 1 para Antioquia): ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_ciudad(nombre, descripcion, estado_id)
        elif tipo_registro == 6:
            nombre = impt.input_animado("Ingrese el nombre de la persona: ", delay=0.01)
            apellido = impt.input_animado("Ingrese el apellido de la persona: ", delay=0.01)
            documento_identidad = impt.input_animado("Ingrese el documento de identidad: ", delay=0.01)
            genero_id = impt.input_animado("Ingrese el ID del género (ejemplo: 1 para Masculino): ", delay=0.01)
            ciudad_id = impt.input_animado("Ingrese el ID de la ciudad (ejemplo: 1 para Medellín): ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_persona(nombre, apellido, documento_identidad, genero_id, ciudad_id)
        elif tipo_registro == 7:
            tipo_telefono = impt.input_animado("Ingrese el tipo de teléfono: ", delay=0.01)
            numero_telefono = impt.input_animado("Ingrese el número de teléfono: ", delay=0.01)
            persona_id = impt.input_animado("Ingrese el ID de la persona (ejemplo: 1): ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_telefono(tipo_telefono, numero_telefono, persona_id)
        elif tipo_registro == 8:
            titulo = impt.input_animado("Ingrese el título del cargo: ", delay=0.01)
            descripcion = impt.input_animado("Ingrese la descripción del cargo: ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_cargo(titulo, descripcion)
        elif tipo_registro == 9:
            nombre = impt.input_animado("Ingrese el nombre de la entidad: ", delay=0.01)
            descripcion = impt.input_animado("Ingrese la descripción de la entidad: ", delay=0.01)
            tipo_entidad = impt.input_animado("Ingrese el tipo de entidad: ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_entidad(nombre, descripcion, tipo_entidad)
        elif tipo_registro == 10:
            persona_id = impt.input_animado("Ingrese el ID de la persona (ejemplo: 1): ", delay=0.01)
            cargo_id = impt.input_animado("Ingrese el ID del cargo (ejemplo: 1): ", delay=0.01)
            entidad_id = impt.input_animado("Ingrese el ID de la entidad (ejemplo: 1): ", delay=0.01)
            fecha_inicio = impt.input_animado("Ingrese la fecha de inicio (YYYY-MM-DD): ", delay=0.01)
            fecha_fin = impt.input_animado("Ingrese la fecha de fin (YYYY-MM-DD): ", delay=0.01)
            estado = impt.input_animado("Ingrese el estado: ", delay=0.01)
            conexion = crear.Conexion()
            conexion.create_asignacion_cargo(persona_id, cargo_id, entidad_id, fecha_inicio, fecha_fin, estado)
        else:
            impt.imprimir_letra_por_letra("Opción no válida, por favor intente nuevamente.", delay=0.01)

    def leer_registros(self):
        conexion: leer.Conexion = leer.Conexion()

        impt.imprimir_letra_por_letra("--Lista de géneros:\n")
        conexion.list_connection_genero()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de usuarios:\n")
        conexion.list_connection_usuario()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de países:\n")
        conexion.list_connection_pais()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de estados:\n")
        conexion.list_connection_estado()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de ciudades:\n")
        conexion.list_connection_ciudad()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de personas:\n")
        conexion.list_connection_persona()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de teléfonos:\n")
        conexion.list_connection_telefono()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de cargos:\n")
        conexion.list_connection_cargo()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de entidades:\n")
        conexion.list_connection_entidad()
        impt.imprimir_letra_por_letra("\n")

        impt.imprimir_letra_por_letra("--Lista de asignaciones de cargos:\n")
        conexion.list_connection_asignacion_cargo()
        impt.imprimir_letra_por_letra("\n")

    def actualizar_registro(self):
        tabla = int(impt.input_animado(
            "Seleccione la tabla que desea actualizar:\n"
            "   1 = Género\n"
            "   2 = Usuario\n"
            "   3 = País\n"
            "   4 = Estado\n"
            "   5 = Ciudad\n"
            "   6 = Persona\n"
            "   7 = Teléfono\n"
            "   8 = Cargo\n"
            "   9 = Entidad\n"
            "   10 = Asignación de Cargo\n"
            "Inserte el número de opción...\n   ", delay=0.03))

        registro_id = impt.input_animado("Ingrese el ID del registro que desea actualizar: ", delay=0.01)

        if tabla == 1:
            nuevo_nombre = impt.input_animado("Ingrese el nuevo nombre del género: ", delay=0.01)
            nueva_descripcion = impt.input_animado("Ingrese la nueva descripción del género: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_genero(registro_id, nuevo_nombre, nueva_descripcion)
        elif tabla == 2:
            nuevo_username = impt.input_animado("Ingrese el nuevo nombre de usuario: ", delay=0.01)
            nuevo_password_hash = impt.input_animado("Ingrese el nuevo hash de la contraseña: ", delay=0.01)
            nuevo_email = impt.input_animado("Ingrese el nuevo email: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_usuario(registro_id, nuevo_username, nuevo_password_hash, nuevo_email)
        elif tabla == 3:
            nuevo_nombre = impt.input_animado("Ingrese el nuevo nombre del país: ", delay=0.01)
            nueva_descripcion = impt.input_animado("Ingrese la nueva descripción del país: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_pais(registro_id, nuevo_nombre, nueva_descripcion)
        elif tabla == 4:
            nuevo_nombre = impt.input_animado("Ingrese el nuevo nombre del estado: ", delay=0.01)
            nueva_descripcion = impt.input_animado("Ingrese la nueva descripción del estado: ", delay=0.01)
            nuevo_pais_id = impt.input_animado("Ingrese el nuevo ID del país: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_estado(registro_id, nuevo_nombre, nueva_descripcion, nuevo_pais_id)
        elif tabla == 5:
            nuevo_nombre = impt.input_animado("Ingrese el nuevo nombre de la ciudad: ", delay=0.01)
            nueva_descripcion = impt.input_animado("Ingrese la nueva descripción de la ciudad: ", delay=0.01)
            nuevo_estado_id = impt.input_animado("Ingrese el nuevo ID del estado: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_ciudad(registro_id, nuevo_nombre, nueva_descripcion, nuevo_estado_id)
        elif tabla == 6:
            nuevo_nombre = impt.input_animado("Ingrese el nuevo nombre de la persona: ", delay=0.01)
            nuevo_apellido = impt.input_animado("Ingrese el nuevo apellido de la persona: ", delay=0.01)
            nuevo_documento_identidad = impt.input_animado("Ingrese el nuevo documento de identidad: ", delay=0.01)
            nuevo_genero_id = impt.input_animado("Ingrese el nuevo ID del género: ", delay=0.01)
            nuevo_ciudad_id = impt.input_animado("Ingrese el nuevo ID de la ciudad: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_persona(registro_id, nuevo_nombre, nuevo_apellido, nuevo_documento_identidad, nuevo_genero_id, nuevo_ciudad_id)
        elif tabla == 7:
            nuevo_tipo_telefono = impt.input_animado("Ingrese el nuevo tipo de teléfono: ", delay=0.01)
            nuevo_numero_telefono = impt.input_animado("Ingrese el nuevo número de teléfono: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_telefono(registro_id, nuevo_tipo_telefono, nuevo_numero_telefono)
        elif tabla == 8:
            nuevo_titulo = impt.input_animado("Ingrese el nuevo título del cargo: ", delay=0.01)
            nueva_descripcion = impt.input_animado("Ingrese la nueva descripción del cargo: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_cargo(registro_id, nuevo_titulo, nueva_descripcion)
        elif tabla == 9:
            nuevo_nombre = impt.input_animado("Ingrese el nuevo nombre de la entidad: ", delay=0.01)
            nueva_descripcion = impt.input_animado("Ingrese la nueva descripción de la entidad: ", delay=0.01)
            nuevo_tipo_entidad = impt.input_animado("Ingrese el nuevo tipo de entidad: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_entidad(registro_id, nuevo_nombre, nueva_descripcion, nuevo_tipo_entidad)
        elif tabla == 10:
            nuevo_persona_id = impt.input_animado("Ingrese el nuevo ID de la persona: ", delay=0.01)
            nuevo_cargo_id = impt.input_animado("Ingrese el nuevo ID del cargo: ", delay=0.01)
            nuevo_entidad_id = impt.input_animado("Ingrese el nuevo ID de la entidad: ", delay=0.01)
            nueva_fecha_inicio = impt.input_animado("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ", delay=0.01)
            nueva_fecha_fin = impt.input_animado("Ingrese la nueva fecha de fin (YYYY-MM-DD): ", delay=0.01)
            nuevo_estado = impt.input_animado("Ingrese el nuevo estado: ", delay=0.01)
            conexion = actualizar.Conexion()
            conexion.update_asignacion_cargo(registro_id, nuevo_persona_id, nuevo_cargo_id, nuevo_entidad_id, nueva_fecha_inicio, nueva_fecha_fin, nuevo_estado)
        else:
            impt.imprimir_letra_por_letra("Opción no válida, por favor intente nuevamente.", delay=0.01)

    def eliminar_registro(self):
        tabla = int(impt.input_animado(
            "Seleccione la tabla de la cual desea eliminar un registro:\n"
            "   1 = Género\n"
            "   2 = Usuario\n"
            "   3 = País\n"
            "   4 = Estado\n"
            "   5 = Ciudad\n"
            "   6 = Persona\n"
            "   7 = Teléfono\n"
            "   8 = Cargo\n"
            "   9 = Entidad\n"
            "   10 = Asignación de Cargo\n"
            "Inserte el número de opción...\n   ", delay=0.03))
        
        registro_id = impt.input_animado("Ingrese el ID del registro que desea eliminar: ", delay=0.01)
        
        conexion = borrar.Conexion()

        if tabla == 1:
            conexion.delete_genero(registro_id)
        elif tabla == 2:
            conexion.delete_usuario(registro_id)
        elif tabla == 3:
            conexion.delete_pais(registro_id)
        elif tabla == 4:
            conexion.delete_estado(registro_id)
        elif tabla == 5:
            conexion.delete_ciudad(registro_id)
        elif tabla == 6:
            conexion.delete_persona(registro_id)
        elif tabla == 7:
            conexion.delete_telefono(registro_id)
        elif tabla == 8:
            conexion.delete_cargo(registro_id)
        elif tabla == 9:
            conexion.delete_entidad(registro_id)
        elif tabla == 10:
            conexion.delete_asignacion_cargo(registro_id)
        else:
            impt.imprimir_letra_por_letra("Opción no válida, por favor intente nuevamente.", delay=0.01)

inicio = Iniciar()