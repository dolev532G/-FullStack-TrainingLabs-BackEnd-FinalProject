from flask import Flask, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from bson import ObjectId
from DAL.convert_mongo_object import convert_mongo_object

from datetime import datetime


class shiftDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["MyDB"] 

    def get_all_shifts(self,filters={}):
        arr = []
        resp = self.__db["shifts"].find(filters)
        for shift in resp : 
            shift["_id"] = str(shift["_id"])
            arr.append(shift)

        
        return convert_mongo_object(arr)

    
    def add_shift(self,obj):
        return self.__db["shifts"].insert_one(obj)

    
    def update_shift(self,id,obj):
        print(str(id))
        return  self.__db["shifts"].update_one(
            { "_id" : ObjectId(id) } ,
            { "$set" : obj }
            )
