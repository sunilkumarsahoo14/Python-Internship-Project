
from flask_marshmallow import Marshmallow
from models import Employee

ma = Marshmallow()

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True

        