from flask import Blueprint,jsonify, request
from BLL.employees_bl import employeeBL

employees = Blueprint('employees', __name__)

employee_bl = employeeBL()

#Get All
@employees.route("/", methods=['GET'])
def get_all_employees():
    employees = employee_bl.get_all_employees()
    return jsonify(employees)

@employees.route("/<string:id>", methods=['GET'])
def get_by_Id(id):
    employees = employee_bl.get_by_Id(id)
    return (employees)


@employees.route("/<string:id>", methods=['PUT'])
def update_employee(id):
    employees = employee_bl.update_employee(id,request.json)
    return (employees)


@employees.route("/EmployeesPage", methods=['GET'])
def GetEmployeesPage():
    employees = employee_bl.GetEmployeesPage()
    return (employees)


@employees.route("/<string:id>", methods=['DELETE'])
def delete_employee(id):
    return employee_bl.delete_employee(id,request.json)
  

@employees.route("/", methods=['POST'])
def add_employee():
    return employee_bl.add_employee(request.json)
  


