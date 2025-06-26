from flask import jsonify
from app.models import Employee
from app import db

class EmployeeRepository:
    @staticmethod
    def get_by_id(employee_id):
        return Employee.query.get(employee_id)

    @staticmethod
    def get_all():
        return Employee.query.all()

    @staticmethod
    def create(data):
        employee = Employee(**data)
        db.session.add(employee)
        db.session.commit()
        return employee

    @staticmethod
    def update(employee_id, data):
        employee = Employee.query.get(employee_id)
        if not employee:
            return None
        for key, value in data.items():
            setattr(employee, key, value)
        db.session.commit()
        return employee

    @staticmethod
    def delete(employee_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return None
        db.session.delete(employee)
        db.session.commit()
        return employee

    @staticmethod
    def remove_manager(employee_id):
        employee = Employee.query.get(employee_id)
        if employee.manager_id is None:
            return None
        if not employee:
            return None
        employee.manager_id = None
        db.session.commit()
        return employee

    @staticmethod
    def assign_manager(employee_id, manager_id):
        employee = Employee.query.get(employee_id)
        if not employee:
            return None
        employee.manager_id = manager_id
        db.session.commit()
        return employee
