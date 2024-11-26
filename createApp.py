from flask import Flask, jsonify, request
from controller.conexion import Conexion

app = Flask(__name__)
conexion = Conexion()

# CREATE endpoints
@app.route('/genero', methods=['POST'])
def create_genero():
    try:
        data = request.json
        created = conexion.create_connection_genero(data['nombre_genero'], data['descripcion'])
        if created:
            return jsonify({"message": "Genero created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Genero"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/usuario', methods=['POST'])
def create_usuario():
    try:
        data = request.json
        created = conexion.create_connection_usuario(data['username'], data['email'])
        if created:
            return jsonify({"message": "Usuario created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Usuario"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/pais', methods=['POST'])
def create_pais():
    try:
        data = request.json
        created = conexion.create_connection_pais(data['nombre_pais'], data['descripcion'])
        if created:
            return jsonify({"message": "Pais created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Pais"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/estado', methods=['POST'])
def create_estado():
    try:
        data = request.json
        created = conexion.create_connection_estado(data['nombre_estado'], data['descripcion'], data['pais_id'])
        if created:
            return jsonify({"message": "Estado created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Estado"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/ciudad', methods=['POST'])
def create_ciudad():
    try:
        data = request.json
        created = conexion.create_connection_ciudad(data['nombre_ciudad'], data['descripcion'], data['estado_id'])
        if created:
            return jsonify({"message": "Ciudad created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Ciudad"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/persona', methods=['POST'])
def create_persona():
    try:
        data = request.json
        created = conexion.create_connection_persona(data['nombre'], data['apellido'], data['ciudad_id'])
        if created:
            return jsonify({"message": "Persona created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Persona"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/telefono', methods=['POST'])
def create_telefono():
    try:
        data = request.json
        created = conexion.create_connection_telefono(data['tipo'], data['numero'], data['persona_id'])
        if created:
            return jsonify({"message": "Telefono created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Telefono"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/cargo', methods=['POST'])
def create_cargo():
    try:
        data = request.json
        created = conexion.create_connection_cargo(data['titulo'], data['descripcion'])
        if created:
            return jsonify({"message": "Cargo created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Cargo"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/entidad', methods=['POST'])
def create_entidad():
    try:
        data = request.json
        created = conexion.create_connection_entidad(data['nombre'], data['descripcion'], data['tipo'])
        if created:
            return jsonify({"message": "Entidad created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Entidad"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/asignacion_cargo', methods=['POST'])
def create_asignacion_cargo():
    try:
        data = request.json
        created = conexion.create_connection_asignacion_cargo(data['estado'], data['fecha_inicio'], data['fecha_fin'], data['persona_id'], data['cargo_id'])
        if created:
            return jsonify({"message": "Asignacion Cargo created successfully"}), 201
        else:
            return jsonify({"error": "Failed to create Asignacion Cargo"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
