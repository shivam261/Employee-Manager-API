from app import db


class Manager(db.Model):
    
    __tablename__ = 'managers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'<Manager {self.name}>'
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'age': self.age
        }




