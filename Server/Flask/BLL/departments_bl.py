from DAL.departments_db_DAL import departmentDBDal
from BLL.Validate_bl import UsersBL

from bson.objectid import ObjectId

from bson.objectid import ObjectId

from flask import Blueprint,jsonify, request, make_response

class departmentsBL:
    def __init__(self):
        self.__departments = departmentDBDal()
        self.__validteBL = UsersBL()
       
    def get_all_departments(self):
       departments = self.__departments.get_all_departments()
       return departments


    def add_department(self,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            
            # Extract employee object from the request body
            department = obj["department"] 
            # Add the employee using EmployeeService
            result = self.__departments.add_department(department)
            print(result.inserted_id)

            return make_response(({"NewId" : str(result.inserted_id)}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)
        

    def update_department(self,id,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            
            # Extract employee object from the request body
            department = obj["department"] 
            # Add the employee using EmployeeService
            result = self.__departments.update_department(id,department)
          

            return make_response(({"Updated" : result.matched_count}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)


    def delete_department(self,id,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            

            # Add the employee using EmployeeService
            result = self.__departments.delete_department(id)
          

            return make_response(({"delted" : result.deleted_count}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)


