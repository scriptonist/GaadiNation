from app import app
from pymongo import MongoClient


def init_db():
    db = MongoClient([app.config['MONGO_URI']])
    collection = db[app.config['DB']][app.config['COLLECTION']]
    return collection


def find_by_car_name(name):
    """ This function returns text search results
        with the argument giver
    """
    collection = init_db()
    res = collection.find({"$text": {"$search": name}}, {
                          "score": {"$meta": "textScore"}}).sort([
                              ("score", {"$meta": "textScore"})
                          ])
    return res


def get_details_of_car(carname):
    """ Get Details about a car by the carname """
    collection = init_db()
    res = collection.find_one({"carname":carname})
    return dict(res)

def filter_car_by_price(end_price,start_price=0):
    """ Function to Filter Cars withing a budget"""
    collection = init_db()
    res = collection.find({"$and":[{"start_price":{'$gte':start_price}},{"end_price":{'$lt':end_price}}]})
    return res

def filter_car_by_mileage(mileage):
    """
    Return a list of cars which has mileage grater than
    or equal to the given parameter
    :param mileage:
    :return: Cursor of mileage greter than mileage
    """
    collection = init_db()
    res = collection.find({'Mileage':{"$gte":mileage}})
    return res

def filter_by_many_values_perfect(conditions=[]):
    collection = init_db()
    if not conditions:
        return collection.find()
    else:
        res = collection.find({"$and": conditions})
        return res

r = filter_by_many_values_perfect([{"BodyType":"Hatchback"}])

for e in r:
    print(e['carname'])




