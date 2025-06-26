from flask import Blueprint, request
from app import limiter
from app.controllers import employee_controller
employee_bp=Blueprint('employee_routes', __name__, url_prefix='/employees')
limiter.limit("10 per minute")(employee_bp)

@employee_bp.route('/<int:employee_id>', methods=['GET', 'PATCH', 'DELETE'])
def get_employee(employee_id):
    if request.method == 'GET':
        return employee_controller.get_employee_by_id(employee_id)
    elif request.method == 'PATCH':
        return employee_controller.update_employee(employee_id)
    elif request.method == 'DELETE':
        return employee_controller.delete_employee(employee_id)

@employee_bp.route('/', methods=['POST','GET'])
def create_employee():
    if request.method == 'GET':
        return employee_controller.get_all_employees()
    elif request.method == 'POST':  
        return employee_controller.create_employee()        

@employee_bp.route('/leave', methods=['POST'])
def leave_manager():
    return employee_controller.leave_manager()

@employee_bp.route('/join', methods=['POST'])
def join_manager():
    return employee_controller.join_manager()

