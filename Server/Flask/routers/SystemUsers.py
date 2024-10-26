from flask import Blueprint,jsonify, request
from BLL.SystemUsers_bl import SystemUsersBL

users = Blueprint('users', __name__)

user_bl = SystemUsersBL()

#Get All
@users.route("/", methods=['GET'])
def get_all_users():
    users = user_bl.get_all_SystemUsers()
    return jsonify(users)

