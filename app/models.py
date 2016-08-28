from app import app
import pymongo
from pymongo import MongoClient


def init_db():
    db = MongoClient([app.config['MONGO_URI']])
    collection = db[app.config['DB']][app.config['COLLECTION']]
    return collection


def find_by_car_name(name):
    collection = init_db()
    res = collection.find({"$text": {"$search": name}}, {
                          "score": {"$meta": "textScore"}}).sort([
                              ("score", {"$meta": "textScore"})
                          ])
    return res


def get_details_of_car(carname):
    collection = init_db()
    res = collection.find_one({"carname":carname})
    return dict(res)

