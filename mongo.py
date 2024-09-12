from datetime import datetime

from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://mongo:strong_password@localhost:27017/database?authSource=admin')


def add_url_to_mongo(short_url:str, long_url:str, user_id:int, created_at:int):

    try:
        client["shortUrls"]["urls"].insert_one({"short_url":short_url,"long_url":long_url,"user_id":user_id,"created_at":created_at})
        return "added_succefully"
    except Exception as e:
        return f'Mongo update failed with error {e}'

def read_from_mongo(short_url:str):
    try:
        result = client["shortUrls"]["urls"].find({"short_url":short_url},{"_id":False,"long_url":True}).limit(1)
        return result[0]["long_url"]

    except Exception as e:
        return f"Failed to get it with error {e}"

result = read_from_mongo(short_url="kB")
print(result)