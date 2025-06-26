from app.repositories.manager_repository import ManagerRepository

class ManagerService:
    @staticmethod
    def get_manager_by_id(manager_id):
        return ManagerRepository.get_by_id(manager_id)

    @staticmethod
    def get_all_managers():
        return ManagerRepository.get_all()

    @staticmethod
    def create_manager(data):
        # check if data is empty
        if not data:
            return None 
        
        valid_keys = {'name', 'salary','age'}
        # check if all valid keys are present in data
        if not valid_keys.issubset(data.keys()):
            return {"error": "missing required fields"} 

        
        return ManagerRepository.create(data)

    @staticmethod
    def update_manager(manager_id, data):
        # check if data is empty
        if not data:
            return None
        valid_keys = {'name', 'salary','age'}
        # check if keys in data are valid but not all keys are required use intersection
        if not valid_keys.intersection(data.keys()):
            return {"error": "some unwanted  fields are present in data"}
        
        
        return ManagerRepository.update(manager_id, data)

    @staticmethod
    def delete_manager(manager_id):
        return ManagerRepository.delete(manager_id)
