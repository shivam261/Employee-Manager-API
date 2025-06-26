from flask import jsonify
from app.models import Manager
from app import db

class ManagerRepository:
    @staticmethod
    def get_by_id(manager_id):
        return Manager.query.get(manager_id)

    @staticmethod
    def get_all():
        return Manager.query.all()

    @staticmethod
    def create(data):
        manager = Manager(**data)
        db.session.add(manager)
        db.session.commit()
        return manager

    @staticmethod
    def update(manager_id, data):
        manager = Manager.query.get(manager_id)
        if not manager:
            return None
        for key, value in data.items():
            setattr(manager, key, value)
        db.session.commit()
        return manager

    @staticmethod
    def delete(manager_id):
        manager = Manager.query.get(manager_id)
        if not manager:
            return None
        db.session.delete(manager)
        db.session.commit()
        return manager
        
