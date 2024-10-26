from flask import Blueprint,jsonify, request
from BLL.shifts_bl import shiftsBL

shifts = Blueprint('shifts', __name__)

shift_bl = shiftsBL()

#Get All
@shifts.route("/", methods=['GET'])
def get_all_shifts():
    shifts = shift_bl.get_all_shifts()
    return shifts


@shifts.route("/", methods=['POST'])
def add_shift():
    return shift_bl.add_shift(request.json)
  
@shifts.route("/<string:id>", methods=['PUT'])
def update_shift(id):
    shift = shift_bl.update_shift(id,request.json)
    return (shift)

@shifts.route("/<string:id>/allocate", methods=['PUT'])
def Allocate_Employee(id):
    shift = shift_bl.Allocate_Employee(id,request.json)
    return (shift)

@shifts.route("/<string:id>", methods=['GET'])
def get_by_Id(id):
    shift = shift_bl.get_by_Id(id)
    return (shift)

