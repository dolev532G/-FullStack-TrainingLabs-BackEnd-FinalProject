from DAL.users_db_DAL import UserDBDal
from BLL.Validate_bl import UsersBL
from DAL.actions_file_DAL import ActionsFileDAL

from bson.objectid import ObjectId
from flask import jsonify, request, make_response
from datetime import datetime


class SystemUsersBL:
    def __init__(self):
        self.__SystemUsers = UserDBDal()
        self.__actionsFile = ActionsFileDAL()

    def get_all_SystemUsers(self):
       SystemUsers = self.__SystemUsers.get_all_users()
       actions = self.__actionsFile.read_file()
        
       today = datetime.now().isoformat(timespec='milliseconds') + 'Z'
       usrsA = []

       for usr in SystemUsers : 
          action_allowed = [
            act for act in actions["actions"]
            if act['id'] == usr['_id'] and today[:10] == act['date'][:10]]
        
          usrsA.append ({
              "FullName" : usr["FullName"],
              "Num_Of_actions" : usr["Num_Of_actions"],
              "currentActions" :  int(usr["Num_Of_actions"]) - len(action_allowed)    
          })

       return usrsA

