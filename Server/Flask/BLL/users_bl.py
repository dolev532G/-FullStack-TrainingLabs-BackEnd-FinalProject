from DAL.users_ws_DAL import UsersWSDAL
from bson.objectid import ObjectId


class UsersBL:
    def __init__(self):
        self.__users = UsersWSDAL()
        
       
    def get_all_users(self):
       users = self.__users.get_all_users()
       return users
