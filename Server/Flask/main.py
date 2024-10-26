from flask import Flask
import json
from bson import ObjectId
from flask_cors import CORS
import sys

from routers.Actions import actions
from routers.SystemUsers import users
from routers.Validation import Validation
from routers.departments import departments
from routers.employees import employees
from routers.shifts import shifts


sys.tracebacklimit=0
    
app = Flask(__name__)

CORS(app)


app.register_blueprint(actions, url_prefix="/actions")
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(Validation, url_prefix="/Validation")
app.register_blueprint(departments, url_prefix="/departments")
app.register_blueprint(employees, url_prefix="/employees")
app.register_blueprint(shifts, url_prefix="/shifts")



app.run(port=5000)

