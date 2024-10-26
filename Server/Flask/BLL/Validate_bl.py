from DAL.users_db_DAL import UserDBDal
from DAL.users_ws_DAL import UsersWSDAL
from DAL.actions_file_DAL import ActionsFileDAL

from flask import jsonify, request
from datetime import datetime
from datetime import timedelta
from bson.objectid import ObjectId

import jwt


class UsersBL:
    def __init__(self):
        self.__usersDB = UserDBDal()
        self.__usersWS = UsersWSDAL()
        self.__actionsFile = ActionsFileDAL()
        self.__SECRET_KEY = "some_key_very_very_secret"

    def get_all_users(self):
       users = self.__usersWS.get_all_users()
       return users

    def validate_user(self,filters):
        # 1. Fetch users from MongoDB (equivalent to ValidationusersRepo.GetUSersPlaceholder)
        all_users = self.__usersWS.get_all_users()
        actions = self.__actionsFile.read_file()
        username = filters.get('username')
        email = filters.get('email')
        
        userV = [user for user in all_users if user["email"] == email and user["username"] == username]


        if userV:
            # 3. If user found, get their full name
            usr = self.__usersDB.get_all_users(filters={"FullName": userV[0]["name"]})  # Fetch user details based on nameusr = self.__usersDB.get_all_users({"FullName": userV[0]["name"]})  # Fetch user details based on name
            

            usrid = usr[0]["_id"]  # Get user ID
            max_actions = usr[0]["Num_Of_actions"]  # Get user's max actions

            # 4. Get today's date
            today = datetime.now().isoformat(timespec='milliseconds') + 'Z'


            # 5. Filter actions based on user ID and today's date
            action_allowed = [
                act for act in actions["actions"]
                if act["id"] == usrid and today[:10] == act["date"][:10]
            ]



            token = {
                "Token":
                 jwt.encode(
                    {
                        "username": username,
                        "email": email,
                        "usrid": usrid,
                        "maxactions": max_actions
                    },
                    self.__SECRET_KEY,
                    algorithm="HS256",  # Specify the algorithm
                ),  # Decode to string if necessary
                "Fullname": userV[0]["name"],  # Assuming userV is defined in your context
                "Num_Of_actions": str(int( max_actions) - len(action_allowed)),
                "Status": "Success"
            }

            # Return or process action_allowed as needed
            return  token

        return []  # Return empty if no user found
    


    def server_request(self, token):

        jt = jwt.decode(token, self.__SECRET_KEY, algorithms=["HS256"])

        # Fetch all users
        all_users = self.__usersWS.get_all_users()
        username = jt['username']
        email = jt['email']
        usrid = jt['usrid']
        maxactions = jt['maxactions']

        userV = [user for user in all_users if user["email"] == email and user["username"] == username]


        if len(userV) > 0:
            # Read actions from the file
            actions_data = self.__actionsFile.read_file()
            today = datetime.now().isoformat(timespec='milliseconds') + 'Z'



            # Filter actions based on user ID and today's date
            action_allowed = [
                act for act in actions_data["actions"]
                if act["id"] == usrid and today[:10] == act["date"][:10]
            ]

            # Check if max actions have been reached
            if maxactions - len(action_allowed) == 0:
                return 0  # No actions allowed
            

            # Add a new action
            actions_data["actions"].append({
                "id": str(usrid),
                "maxActions": maxactions,
                "date": str(today),
                "actionAllowed": maxactions - len(action_allowed)
            })

            self.__actionsFile.write_file(actions_data)  # Ensure this is also async
            return 1 


        
        