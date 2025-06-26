from flask import request, jsonify
from app.services.employee_service import EmployeeService
from app.services.manager_service import ManagerService
from app import cache
def get_employee_by_id(employee_id):
    emp = EmployeeService.get_employee_by_id(employee_id)
    return jsonify(emp.to_dict()) if emp else (jsonify({"error": "Not found"}), 404)

def get_all_employees():
    if cache.get('all_employees'):
        return jsonify(cache.get('all_employees')), 200
    emps = EmployeeService.get_all_employees()
    cache.set('all_employees', [e.to_dict() for e in emps], timeout=10)  # Cache for 60 seconds
    return jsonify([e.to_dict() for e in emps]), 200

def create_employee():
    data = request.get_json()
    emp = EmployeeService.create_employee(data)
    if isinstance(emp, dict) and "error" in emp:
        return jsonify(emp), 400  # Return error if data is invalid
    return jsonify(emp.to_dict()), 201

def update_employee(employee_id):
    data = request.get_json()
    emp = EmployeeService.update_employee(employee_id, data)
    return jsonify(emp.to_dict()) if emp else (jsonify({"error": "Employee not found "}), 404)

def delete_employee(employee_id):
    emp = EmployeeService.delete_employee(employee_id)
    if not emp:
        return jsonify({"error": f"Employee not found with id {employee_id}"}), 404
    return (jsonify({"message": f"Employee deleted successfully with id {employee_id}"}), 200)

def leave_manager():
    data = request.get_json()
    emp_id = data.get("employee_id")
    emp = EmployeeService.leave_manager(emp_id)
    return jsonify(emp.to_dict()) if emp else (jsonify({"error": "employee not found or already dont have manager"}), 404)

def join_manager():
    data = request.get_json()
    emp_id = data.get("employee_id")
    mgr_id = data.get("manager_id")
    e=EmployeeService.get_employee_by_id(emp_id)
    m=ManagerService.get_manager_by_id(mgr_id)
    if not emp_id or not mgr_id:
        return jsonify({"error": "Employee ID and Manager ID are required"}), 400
    if not e or not m:
        return jsonify({"error": "Employee or Manager not found"}), 404
    
    emp = EmployeeService.join_manager(emp_id, mgr_id)

    return jsonify(emp.to_dict()) if emp else (jsonify({"error": "Not found"}), 404)
