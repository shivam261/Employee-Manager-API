from flask import request, jsonify
from app.services.manager_service import ManagerService
from app.models import Employee

def get_manager_by_id(manager_id):
    manager = ManagerService.get_manager_by_id(manager_id)
    return (jsonify(manager.to_dict()), 200) if manager else (jsonify({"error": "Manager not found"}), 404)

def get_all_managers():
    managers = ManagerService.get_all_managers()
    return jsonify([m.to_dict() for m in managers]), 200

def create_manager():
    data = request.get_json()
    manager = ManagerService.create_manager(data)
    if isinstance(manager, dict) and "error" in manager:
        return jsonify(manager), 400  # Return error if data is invalid
    
    return jsonify(manager.to_dict()), 201

def update_manager(manager_id):
    data = request.get_json()
    manager = ManagerService.update_manager(manager_id, data)
    if isinstance(manager, dict) and "error" in manager:
        return jsonify(manager), 400  # Return error if data is invalid
    return (jsonify(manager.to_dict()), 200) if manager else (jsonify({"error": "Manager not found"}), 404)

def delete_manager(manager_id):

    manager= ManagerService.delete_manager(manager_id)
    if not manager:
        return jsonify({"error": "Manager not found"}), 404
    return (jsonify({"message": f"Manager deleted successfully with id {manager_id}"}), 200)



def get_employees_by_manager(manager_id):
    employees = Employee.query.filter_by(manager_id=manager_id).all()
    return jsonify([e.to_dict() for e in employees]), 200
