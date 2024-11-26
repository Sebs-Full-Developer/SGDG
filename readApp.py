from flask import Flask, jsonify
from controller.conexion import Conexion

app = Flask(__name__)
conexion = Conexion()

@app.route('/genero', methods=['GET'])
def get_genero():
    data = conexion.list_connection_genero()
    return jsonify([{"id": d.GetId(), "nombre_genero": d.GetNombreGenero(), "descripcion": d.GetDescripcion()} for d in data])

@app.route('/usuario', methods=['GET'])
def get_usuario():
    data = conexion.list_connection_usuario()
    return jsonify([{"id": d.GetId(), "username": d.GetUsername(), "email": d.GetEmail()} for d in data])

@app.route('/pais', methods=['GET'])
def get_pais():
    data = conexion.list_connection_pais()
    return jsonify([{"id": d.GetId(), "nombre_pais": d.GetNombrePais(), "descripcion": d.GetDescripcion()} for d in data])

@app.route('/estado', methods=['GET'])
def get_estado():
    data = conexion.list_connection_estado()
    return jsonify([{"id": d.GetId(), "nombre_estado": d.GetNombreEstado(), "descripcion": d.GetDescripcion()} for d in data])

@app.route('/ciudad', methods=['GET'])
def get_ciudad():
    data = conexion.list_connection_ciudad()
    return jsonify([{"id": d.GetId(), "nombre_ciudad": d.GetNombreCiudad(), "descripcion": d.GetDescripcion()} for d in data])

@app.route('/persona', methods=['GET'])
def get_persona():
    data = conexion.list_connection_persona()
    return jsonify([{"id": d.GetId(), "nombre_persona": d.GetNombrePersona(), "apellido_persona": d.GetApellidoPersona()} for d in data])

@app.route('/telefono', methods=['GET'])
def get_telefono():
    data = conexion.list_connection_telefono()
    return jsonify([{"id": d.GetId(), "tipo_telefono": d.GetTipoTelefono(), "numero_telefono": d.GetNumeroTelefono()} for d in data])

@app.route('/cargo', methods=['GET'])
def get_cargo():
    data = conexion.list_connection_cargo()
    return jsonify([{"id": d.GetId(), "titulo": d.GetTitulo(), "descripcion": d.GetDescripcion()} for d in data])

@app.route('/entidad', methods=['GET'])
def get_entidad():
    data = conexion.list_connection_entidad()
    return jsonify([{"id": d.GetId(), "nombre_entidad": d.GetNombreEntidad(), "descripcion": d.GetDescripcion(), "tipo_entidad": d.GetTipoEntidad()} for d in data])

@app.route('/asignacion_cargo', methods=['GET'])
def get_asignacion_cargo():
    data = conexion.list_connection_asignacion_cargo()
    return jsonify([{"id": d.GetId(), "estado": d.GetEstado(), "fecha_inicio": d.GetFechaInicio(), "fecha_fin": d.GetFechaFin()} for d in data])

if __name__ == '__main__':
    app.run(debug=True)
