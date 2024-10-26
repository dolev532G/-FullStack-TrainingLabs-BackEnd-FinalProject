from flask import Blueprint,jsonify, request
from BLL.Validate_bl import UsersBL

Validation = Blueprint('Validation', __name__)

user_bl = UsersBL()

#Get All
@Validation.route("/", methods=['GET'])
def getallusers():
    users = user_bl.get_all_users()
    return jsonify(users)

@Validation.route('/', methods=['POST'])
def validate():
    filters = request.json  # Assuming the request contains the filters in JSON format
    response = user_bl.validate_user(filters)
    return response