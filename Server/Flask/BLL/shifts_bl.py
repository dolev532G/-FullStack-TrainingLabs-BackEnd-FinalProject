from DAL.shifts_db_DAL  import shiftDBDal
from bson.objectid import ObjectId
from BLL.Validate_bl import UsersBL

from bson.objectid import ObjectId
from flask import Blueprint,jsonify, request, make_response


class shiftsBL:
    def __init__(self):
        self.__shifts = shiftDBDal()
        self.__validteBL = UsersBL()


    def get_all_shifts(self):
       shifts = self.__shifts.get_all_shifts()
       return shifts
    
    def get_by_Id(self,id):
       shift = self.__shifts.get_all_shifts({"_id" : ObjectId(id)})
       if len(shift) > 0:
            return make_response ( shift[0] , 200)
       else:
           return make_response ({} , 404)


    

    def add_shift(self,obj):          
        try:

            token = obj["token"]            

            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            
            # Extract employee object from the request body
            shift = obj["shift"] 
            # Add the employee using EmployeeService
            result = self.__shifts.add_shift(shift)

            return make_response(({"NewId" : str(result.inserted_id)}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)
        

    def update_shift(self,id,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            
            # Extract employee object from the request body
            shift = obj["shift"] 
            # Add the employee using EmployeeService
            result = self.__shifts.update_shift(id,shift)
          

            return make_response(({"Updated" : result.matched_count}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)


    def Allocate_Employee(self,id,obj):  
        try:
            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            

            # Find the shift by its ID
            shift_document = self.__shifts.get_all_shifts({"_id" : ObjectId(id)})
            employee_id = obj["shift"]["employeeId"]

            # Check if the employee is already in the ID array
            if employee_id in shift_document[0]["ID"]:
                return make_response( 'Employee is already allocated to this shift', 500)
            
            
            shift_document[0]["ID"].append(employee_id)
            del shift_document[0]["_id"]
            print (shift_document[0])

            result = self.__shifts.update_shift(id, shift_document[0])


            if result.matched_count == 1:
                return make_response (  {
                    'message': 'Employee allocated successfully',
                    'updatedShift': result.matched_count
                }, 200)
            else:
                return make_response ( {'message': 'Failed to update shift'}, 500)
        
        except Exception as err:
            return  make_response ( {'message': f"Error adding employee ID: {str(err)}"} , 500)
            
