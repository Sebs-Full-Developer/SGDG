from flask import Blueprint, jsonify, request
from controller.conexion import Conexion

genero_bp = Blueprint('genero', __name__)
conexion = Conexion()

# CREATE
@genero_bp.route('/genero', methods=['POST'])
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

# READ
@genero_bp.route('/genero', methods=['GET'])
def read_genero():
    try:
        generos = conexion.list_connection_genero()
        return jsonify([{
            "id": genero.GetId(),
            "nombre_genero": genero.GetNombreGenero(),
            "descripcion": genero.GetDescripcion()
        } for genero in generos])
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# UPDATE
@genero_bp.route('/genero/<int:genero_id>', methods=['PUT'])
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

# DELETE
@genero_bp.route('/genero/<int:genero_id>', methods=['DELETE'])
def delete_genero(genero_id):
    try:
        deleted = conexion.delete_connection_genero(genero_id)
        if deleted:
            return jsonify({"message": "Genero deleted successfully"}), 200
        else:
            return jsonify({"error": "Genero not found or delete failed"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
