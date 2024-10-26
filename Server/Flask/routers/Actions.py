from flask import Blueprint,jsonify, request
from DAL.actions_bl import ActionsBL

actions = Blueprint('actions', __name__)

actions_bl = ActionsBL()

#Get All
@actions.route("/", methods=['GET'])
def get_all_products():
    products = actions_bl.get_all_actions()
    return jsonify(products)

