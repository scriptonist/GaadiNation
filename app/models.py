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
                          "score": {"$meta": "textScore"}}).limit(8).sort([
                              ("score", {"$meta": "textScore"})
                          ])
    return res


def get_details_of_car(carname):
    """ Get Details about a car by the carname """
    collection = init_db()
    res = collection.find_one({"carname": carname})
    return dict(res)


def filter_car_by_price(end_price, start_price=0):
    """ Function to Filter Cars withing a budget"""
    collection = init_db()
    res = collection.find({"$and": [{"start_price": {'$gte': start_price}}, {
                          "end_price": {'$lt': end_price}}]})
    return res


def filter_car_by_mileage(mileage):
    """
    Return a list of cars which has mileage grater than
    or equal to the given parameter
    :param mileage:
    :return: Cursor of mileage greter than mileage
    """
    collection = init_db()
    res = collection.find({'Mileage': {"$gte": mileage}})
    return res


def filter_by_many_values_perfect(conditions=[]):
    """
    Execute a $and query with the conditions as the argument
    it returns a cursor which follows conditions according to
    the module
    :param conditions:
    :return a cursor with data:
    """
    collection = init_db()
    if not conditions:
        return collection.find()
    else:
        res = collection.find({"$and": conditions})
        return res

def filter_by_args(brand="",prices="",bodytype=""):
    """
    Execute a $and query with the conditions as the argument
    it returns a cursor which follows conditions according to
    the module
    :param conditions:
    :return a cursor with data:
    """
    """
        prices come in format "0-5,10-15" 
        it is converted to a list and converted to 
        interger value in lakhs 
    """
    collection = init_db()
    conditions = []
    if len(prices) > 0:
        prices = prices.split(',')
        print(prices)
        price_filter = []
        for price in prices:
            two_prices = price.split('-')
            two_prices[0] = int(two_prices[0]+"00000")
            two_prices[1] = int(two_prices[1]+"00000") 
            price_filter.append({"start_price":{"$gte":two_prices[0],"$lte":two_prices[1]}})
        price_filter = {"$or":price_filter}
        conditions.append(price_filter)

    if len(brand) > 0:
        brand_filter = {"brand":{"$in":brand.split(',')}}
        conditions.append(brand_filter)

    if len(bodytype) > 0:
        bodytype_filter = {"BodyType":{"$in":bodytype.split(',')}}
        conditions.append(bodytype_filter)
             
    if not conditions:
        return collection.find()
    else:
        res = collection.find({"$and": conditions},)
        return res



def getmanufacturer():
    mname = []
    collection = init_db()
    res = collection.find({}, {'carname': 1, '_id': 0})
    for i in res:
        mname.append(i['carname'].split()[0])
    return set(list(mname))


def getcars(brand):
    collection = init_db()
    res1 = collection.find({"$text": {"$search": brand}}, {
                           'carname': 1, '_id': 0})
    cars = []
    for i in res1:
        cars.append(i['carname'])
    return cars


def getcardetails(carname):
    collection = init_db()
    res = collection.find_one({"carname": carname})
    if(res == None):
        res = {}
    return res
