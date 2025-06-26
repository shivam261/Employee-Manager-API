from app import db


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('managers.id', ondelete='SET NULL'), nullable=True)

    def __repr__(self):
        return f'<Employee {self.name}>'
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'manager_id': self.manager_id
        }