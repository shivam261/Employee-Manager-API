from flask import Blueprint, request
from app import limiter
from app.controllers import manager_controller
manager_bp=Blueprint('manager_routes', __name__, url_prefix='/managers')
limiter.limit("20 per minute")(manager_bp)


@manager_bp.route('/', methods=['GET','POST'])
def get_managers():
    if request.method == 'GET':
        return manager_controller.get_all_managers()
    elif request.method == 'POST':
        return manager_controller.create_manager()

@manager_bp.route('/<int:manager_id>', methods=['GET', 'PATCH', 'DELETE'])
def manage_manager(manager_id):
    if request.method == 'GET':
        return manager_controller.get_manager_by_id(manager_id)
    elif request.method == 'PATCH':
        return manager_controller.update_manager(manager_id)
    elif request.method == 'DELETE':
        return manager_controller.delete_manager(manager_id)
    
@manager_bp.route('/<int:manager_id>/employees', methods=['GET'])   
def get_employees_by_manager(manager_id):
    return manager_controller.get_employees_by_manager(manager_id)
