from DAL.actions_file_DAL import ActionsFileDAL
from bson.objectid import ObjectId

class ActionsBL:
    def __init__(self):
        self.__actions = ActionsFileDAL()
       
    def get_all_actions(self):
       data = self.__actions.read_file()
       return data["actions"]
