from flask import Blueprint,jsonify, request, make_response
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from datetime import datetime

class employeeDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["MyDB"] 

    def get_all_employees(self, id={}):
        
        arr = []
        resp = self.__db["employees"].find(id)
        for employee in resp : 
            employee["_id"] = str(employee["_id"])
            if   "DepartmentID" in employee:
                employee["DepartmentID"] = str(employee["DepartmentID"])
            
            arr.append(employee)

        return arr
    
    def add_employee(self,obj):
        employee = obj
        if  "DepartmentID" in employee:
            employee["DepartmentID"] = ObjectId(employee["DepartmentID"])

        return self.__db["employees"].insert_one(employee)

    

    def update_employee(self,id,obj):
        employee = obj
        
        if  "DepartmentID" in employee:
            employee["DepartmentID"] = ObjectId(employee["DepartmentID"])

        return  self.__db["employees"].update_one(
            { "_id" : ObjectId(id) } ,
            { "$set" : employee }
            )
    
    def delete_employee(self,id):
        return  self.__db["employees"].delete_one(
            { "_id" : ObjectId(id) } 
            )

