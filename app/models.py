from app import app
import pymongo
from pymongo import MongoClient

db = MongoClient()[app.config['DB']]
collection = db[app.config['COLLECTION']]


def find_by_car_name(name):
    res = collection.find({"$text": {"$search": name}}, {
                          "score": {"$meta": "textScore"}}).sort([
                          ("score",{"$meta": "textScore"})
                          ])
    return res
