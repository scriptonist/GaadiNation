from app import app
import pymongo
from pymongo import MongoClient


def initDb():
    db = MongoClient()[app.config['DB']]
    collection = db[app.config['COLLECTION']]
    return(collection)


def find_by_car_name(name):
    collection = initDb()
    res = collection.find({"$text": {"$search": name}}, {
                          "score": {"$meta": "textScore"}}).sort([
                              ("score", {"$meta": "textScore"})
                          ])
    return res
