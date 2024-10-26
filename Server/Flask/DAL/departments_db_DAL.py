from flask import Flask, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from datetime import datetime

class departmentDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["MyDB"] 

    def get_all_departments(self):
        
        arr = []
        resp = self.__db["departments"].find()
        for department in resp : 
            department["_id"] = str(department["_id"])
            department["Manager"] = str(department["Manager"])
            
            arr.append(department)

        return arr
    
    def add_department(self,obj):
        department = obj
        if  "Manager" in department:
            department["Manager"] = ObjectId(department["Manager"])

        return self.__db["departments"].insert_one(department)
    

    def update_department(self,id,obj):
        department = obj
        
        if  "Manager" in department:
            department["Manager"] = ObjectId(department["Manager"])


        return  self.__db["departments"].update_one(
            { "_id" : ObjectId(id) } ,
            { "$set" : department }
            )
    
    def delete_department(self,id):
        return  self.__db["departments"].delete_one(
            { "_id" : ObjectId(id) } 
            )

