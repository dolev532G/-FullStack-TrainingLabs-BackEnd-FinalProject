from flask import Blueprint,jsonify, request
from BLL.departments_bl import departmentsBL

departments = Blueprint('departments', __name__)

department_bl = departmentsBL()

#Get All
@departments.route("/", methods=['GET'])
def get_all_departments():
    departments = department_bl.get_all_departments()
    return jsonify(departments)


@departments.route("/", methods=['POST'])
def add_department():
    return department_bl.add_department(request.json)
  

@departments.route("/<string:id>", methods=['PUT'])
def update_department(id):
    return department_bl.update_department(id,request.json)
  
@departments.route("/<string:id>", methods=['DELETE'])
def delete_department(id):
    return department_bl.delete_department(id,request.json)
  



