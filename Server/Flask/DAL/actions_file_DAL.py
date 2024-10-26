import json
import os
import sys

class ActionsFileDAL:
    def __init__(self):
        self.__path = os.path.join(sys.path[0],'../Data/System_Users_Actions.json')

    def read_file(self):
        with open(self.__path,'r') as f:
            data = json.load(f)
            return data
        
    def write_file(self,obj):
        with open(self.__path,'w') as f:
            json.dump(obj , f)
        

    