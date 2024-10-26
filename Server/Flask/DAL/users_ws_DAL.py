import requests


class UsersWSDAL:
    def __init__(self):
        self.__url = "https://jsonplaceholder.typicode.com/users"

    def get_all_users(self):
        return requests.get(self.__url).json()
        

