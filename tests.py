import unittest
import math,random
from app import app
from app import models
from pymongo import MongoClient


class test_app_search(unittest.TestCase):
    def setUp(self):
        """ Initialize the environment for tests """
        # -------------Get Oroginal Dataset from database -----------------#
        self.connection = MongoClient()
        cars = MongoClient().cars.cars
        # -----------------------------------------------------------------#

        # --------------------Changing App Config for Testing --------------#
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DB'] = "test_cars"
        app.config['COLLECTION'] = "test_cars"
        # ------------------------------------------------------------------#

        # Make sure data base is clean
        self.connection.drop_database(app.config['DB'])

        # Initialise collection variable with app config and create index
        self.collection = models.initDb()
        self.collection.create_index([("carname","text")])

        # Insert the data in original database to test_database
        self.collection.insert_many(cars.find())

    def tearDown(self):
        """ Remove the testing config and clean database """
        self.connection.drop_database(app.config['DB'])
        app.config['TESTING'] = False
        app.config['WTF_CSRF_ENABLED'] = True
        app.config['DB'] = "cars"
        app.config['COLLECTION'] = "cars"

    def get_random_document(self):
        """ Return a random document from the collection """

        # ------------------------------------------------#
        # Get total count of documents in the collection
        # get a random number less than the count
        n = self.collection.count()
        R = math.floor(random.randrange(n))
        # ----------------------------------------------- #
        document = self.collection.find().limit(1).skip(R)
        return document

    def test_find_by_carname_returns_correct_results(self):
        """ Check if the models.py gives correct result on query """
        #Import module to be tested
        from app.models import find_by_car_name
        
        # -------------------Get a search String--------- #
        # a document is returned as a cursor from the get_random_document method
        # It is iterated to find the carname and stored to search_string
        search_string = [string['carname'] for string in self.get_random_document()][0]
        # ----------------------------------------------- #

        # To check if all parts of the search string will be matched 
        # the string is split with respect to spaces and checked for match
        search_string_list = search_string.split()
        for query in search_string_list:
            result = find_by_car_name(query)
            carname_list = [entry['carname'] for entry in result]
            self.assertIn(str(search_string), carname_list)


if __name__ == "__main__":
    unittest.main()
