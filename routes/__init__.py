
from flask import Blueprint, jsonify, request
from models import db, Employee
from schemas import EmployeeSchema

main = Blueprint('main', __name__)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

@main.route('/')
def index():
    return "Welcome to the Employee Management System"

@main.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return employees_schema.jsonify(employees)

@main.route('/employees', methods=['POST'])
def add_employee():
    name = request.json['name']
    position = request.json['position']
    department = request.json['department']
    
    new_employee = Employee(name=name, position=position, department=department)
    db.session.add(new_employee)
    db.session.commit()
    
    return employee_schema.jsonify(new_employee), 201

@main.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    employee.name = request.json['name']
    employee.position = request.json['position']
    employee.department = request.json['department']
    
    db.session.commit()
    return employee_schema.jsonify(employee)

@main.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    
    return '', 204