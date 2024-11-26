from flask import Flask, jsonify
from controller.conexion import Conexion

app = Flask(__name__)
conexion = Conexion()

@app.route('/genero/<int:id>', methods=['DELETE'])
def delete_genero(id):
    try:
        deleted = conexion.delete_connection_genero(id)
        if deleted:
            return jsonify({"message": "Genero deleted successfully"}), 200
        else:
            return jsonify({"error": "Genero not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        deleted = conexion.delete_connection_usuario(id)
        if deleted:
            return jsonify({"message": "Usuario deleted successfully"}), 200
        else:
            return jsonify({"error": "Usuario not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/pais/<int:id>', methods=['DELETE'])
def delete_pais(id):
    try:
        deleted = conexion.delete_connection_pais(id)
        if deleted:
            return jsonify({"message": "Pais deleted successfully"}), 200
        else:
            return jsonify({"error": "Pais not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/estado/<int:id>', methods=['DELETE'])
def delete_estado(id):
    try:
        deleted = conexion.delete_connection_estado(id)
        if deleted:
            return jsonify({"message": "Estado deleted successfully"}), 200
        else:
            return jsonify({"error": "Estado not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/ciudad/<int:id>', methods=['DELETE'])
def delete_ciudad(id):
    try:
        deleted = conexion.delete_connection_ciudad(id)
        if deleted:
            return jsonify({"message": "Ciudad deleted successfully"}), 200
        else:
            return jsonify({"error": "Ciudad not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/persona/<int:id>', methods=['DELETE'])
def delete_persona(id):
    try:
        deleted = conexion.delete_connection_persona(id)
        if deleted:
            return jsonify({"message": "Persona deleted successfully"}), 200
        else:
            return jsonify({"error": "Persona not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/telefono/<int:id>', methods=['DELETE'])
def delete_telefono(id):
    try:
        deleted = conexion.delete_connection_telefono(id)
        if deleted:
            return jsonify({"message": "Telefono deleted successfully"}), 200
        else:
            return jsonify({"error": "Telefono not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/cargo/<int:id>', methods=['DELETE'])
def delete_cargo(id):
    try:
        deleted = conexion.delete_connection_cargo(id)
        if deleted:
            return jsonify({"message": "Cargo deleted successfully"}), 200
        else:
            return jsonify({"error": "Cargo not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/entidad/<int:id>', methods=['DELETE'])
def delete_entidad(id):
    try:
        deleted = conexion.delete_connection_entidad(id)
        if deleted:
            return jsonify({"message": "Entidad deleted successfully"}), 200
        else:
            return jsonify({"error": "Entidad not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/asignacion_cargo/<int:id>', methods=['DELETE'])
def delete_asignacion_cargo(id):
    try:
        deleted = conexion.delete_connection_asignacion_cargo(id)
        if deleted:
            return jsonify({"message": "Asignacion Cargo deleted successfully"}), 200
        else:
            return jsonify({"error": "Asignacion Cargo not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
