from flask import Flask, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from datetime import datetime

class UserDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["MyDB"] 

    def get_all_users(self,filters = {}):
        
        arr = []
        resp = self.__db["users"].find(filters)
        for user in resp : 
            user["_id"] = str(user["_id"])
            arr.append(user)

        return arr
    
    def add_user(self,obj):
        self.__db["users"].insert_one(obj)

    
