from DAL.employee_db_DAL import employeeDBDal
from DAL.departments_db_DAL import departmentDBDal
from DAL.shifts_db_DAL import shiftDBDal


from BLL.Validate_bl import UsersBL

from bson.objectid import ObjectId
from flask import Blueprint,jsonify, request, make_response

class employeeBL:
    def __init__(self):
        self.__employee = employeeDBDal()
        self.__department = departmentDBDal()
        self.__shift = shiftDBDal()

        self.__validteBL = UsersBL()
       
    def get_all_employees(self):
       employee = self.__employee.get_all_employees()
       return employee
    
    def get_by_Id(self,id):
       employee = self.__employee.get_all_employees({"_id" : ObjectId(id)})
       if len(employee) > 0:
            return make_response ( employee[0] , 200)
       else:
           return make_response ({} , 404)
       
    def GetEmployeesPage(self):
        employees =  self.__employee.get_all_employees() # Fetch all employees
        departments =  self.__department.get_all_departments()  # Fetch all departments
        shifts =  self.__shift.get_all_shifts()  # Fetch all shifts

        e_page = []  # Initialize the page list

        for element in employees:
            # Filter the department based on DepartmentID
            dep = [d for d in departments if d['_id'] == element['DepartmentID']]

            # Filter shifts for the current employee's ID
            shifts_for_id = [
                {
                    "_id" : str(x['_id']),
                    "Date": x['Date'],
                    "StartingHour": str(x['StartingHour']),
                    "EndingHour": str(x['EndingHour'])
                }
                for x in shifts if any(s1 == element['_id'] for s1 in x['ID'])
            ]

            # Append the formatted employee data to e_page
            e_page.append({
                "Id": str(element['_id']),
                "Full name": f"{element['FirstName']} {element['LastName']}",
                "Department": dep[0]['Name'] if dep else "Not assigned",
                "Shifts": shifts_for_id
            })

        return e_page


    def add_employee(self,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            
            # Extract employee object from the request body
            employee = obj["employee"] 
            # Add the employee using EmployeeService
            result = self.__employee.add_employee(employee)
            print(result.inserted_id)

            return make_response(({"NewId" : str(result.inserted_id)}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)

    
    def update_employee(self,id,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            
            # Extract employee object from the request body
            employee = obj["employee"] 
            # Add the employee using EmployeeService
            print(id)
            result = self.__employee.update_employee(id,employee)
          

            return make_response(({"Updated" : result.matched_count}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)

    def delete_employee(self,id,obj):  
        try:

            token = obj["token"]
            # Validate the request using ValidationService
            valid_req = self.__validteBL.server_request(token)

            if valid_req == 0:
                # If validation fails, return a 500 status with a message
                return make_response ( ({ "error" : str("Can't do another action today")}) , 500)
            

            # Add the employee using EmployeeService
            result = self.__employee.delete_employee(id)
          

            return make_response(({"delted" : result.deleted_count}),200)


        except Exception as error:
            # If any error occurs, return a 500 status with the error message
            return make_response({"error" : error},500)