from flask import Flask, jsonify, request
from controller.conexion import Conexion

app = Flask(__name__)
conexion = Conexion()

# UPDATE endpoints
@app.route('/genero/<int:genero_id>', methods=['PUT'])
def update_genero(genero_id):
    try:
        data = request.json
        updated = conexion.update_connection_genero(genero_id, data['nombre_genero'], data['descripcion'])
        if updated:
            return jsonify({"message": "Genero updated successfully"}), 200
        else:
            return jsonify({"error": "Genero not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/usuario/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    try:
        data = request.json
        updated = conexion.update_connection_usuario(usuario_id, data['username'], data['email'])
        if updated:
            return jsonify({"message": "Usuario updated successfully"}), 200
        else:
            return jsonify({"error": "Usuario not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/pais/<int:pais_id>', methods=['PUT'])
def update_pais(pais_id):
    try:
        data = request.json
        updated = conexion.update_connection_pais(pais_id, data['nombre_pais'], data['descripcion'])
        if updated:
            return jsonify({"message": "Pais updated successfully"}), 200
        else:
            return jsonify({"error": "Pais not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/estado/<int:estado_id>', methods=['PUT'])
def update_estado(estado_id):
    try:
        data = request.json
        updated = conexion.update_connection_estado(estado_id, data['nombre_estado'], data['descripcion'], data['pais_id'])
        if updated:
            return jsonify({"message": "Estado updated successfully"}), 200
        else:
            return jsonify({"error": "Estado not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/ciudad/<int:ciudad_id>', methods=['PUT'])
def update_ciudad(ciudad_id):
    try:
        data = request.json
        updated = conexion.update_connection_ciudad(ciudad_id, data['nombre_ciudad'], data['descripcion'], data['estado_id'])
        if updated:
            return jsonify({"message": "Ciudad updated successfully"}), 200
        else:
            return jsonify({"error": "Ciudad not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/persona/<int:persona_id>', methods=['PUT'])
def update_persona(persona_id):
    try:
        data = request.json
        updated = conexion.update_connection_persona(persona_id, data['nombre'], data['apellido'], data['ciudad_id'])
        if updated:
            return jsonify({"message": "Persona updated successfully"}), 200
        else:
            return jsonify({"error": "Persona not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/telefono/<int:telefono_id>', methods=['PUT'])
def update_telefono(telefono_id):
    try:
        data = request.json
        updated = conexion.update_connection_telefono(telefono_id, data['tipo'], data['numero'], data['persona_id'])
        if updated:
            return jsonify({"message": "Telefono updated successfully"}), 200
        else:
            return jsonify({"error": "Telefono not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/cargo/<int:cargo_id>', methods=['PUT'])
def update_cargo(cargo_id):
    try:
        data = request.json
        updated = conexion.update_connection_cargo(cargo_id, data['titulo'], data['descripcion'])
        if updated:
            return jsonify({"message": "Cargo updated successfully"}), 200
        else:
            return jsonify({"error": "Cargo not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/entidad/<int:entidad_id>', methods=['PUT'])
def update_entidad(entidad_id):
    try:
        data = request.json
        updated = conexion.update_connection_entidad(entidad_id, data['nombre'], data['descripcion'], data['tipo'])
        if updated:
            return jsonify({"message": "Entidad updated successfully"}), 200
        else:
            return jsonify({"error": "Entidad not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/asignacion_cargo/<int:asignacion_cargo_id>', methods=['PUT'])
def update_asignacion_cargo(asignacion_cargo_id):
    try:
        data = request.json
        updated = conexion.update_connection_asignacion_cargo(asignacion_cargo_id, data['estado'], data['fecha_inicio'], data['fecha_fin'], data['persona_id'], data['cargo_id'])
        if updated:
            return jsonify({"message": "Asignacion Cargo updated successfully"}), 200
        else:
            return jsonify({"error": "Asignacion Cargo not found or update failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
