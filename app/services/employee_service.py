from flask import jsonify
from app.repositories.employee_repository import EmployeeRepository

class EmployeeService:
    @staticmethod
    def get_employee_by_id(employee_id):
        return EmployeeRepository.get_by_id(employee_id)

    @staticmethod
    def get_all_employees():
        return EmployeeRepository.get_all()

    @staticmethod
    def create_employee(data):
        # check if data is empty
        if not data:
            return None 
    
        valid_keys = {'name', 'salary'} 
         # check if data all  valid keys is present in data
        if not valid_keys.issubset(data.keys()):
            return {"error":"missing required fields "}

        
        return EmployeeRepository.create(data)

    @staticmethod
    def update_employee(employee_id, data):
        # check if data is empty
        if not data:
            return None 
        #check if data has valid keys
        valid_keys = {'name','salary', 'manager_id'}
        if not valid_keys.intersection(data.keys()):
            return None
        return EmployeeRepository.update(employee_id, data)

    @staticmethod
    def delete_employee(employee_id):
        return EmployeeRepository.delete(employee_id)

    @staticmethod
    def leave_manager(employee_id):
        return EmployeeRepository.remove_manager(employee_id)

    @staticmethod
    def join_manager(employee_id, manager_id):
        return EmployeeRepository.assign_manager(employee_id, manager_id)
