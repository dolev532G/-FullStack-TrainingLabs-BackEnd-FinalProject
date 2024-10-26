from bson import ObjectId
from datetime import datetime
from bson import ObjectId
import json

def convert_mongo_object(obj):
    if isinstance(obj, dict):
        return {key: convert_mongo_object(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_mongo_object(element) for element in obj]
    elif isinstance(obj, ObjectId):
        return str(obj)  # Convert ObjectId to string
    elif isinstance(obj, datetime):
        return obj.isoformat() + 'Z'  # Convert datetime to ISO format
    elif isinstance(obj, int):
        return obj  # Handle NumberInt as normal int
    return obj