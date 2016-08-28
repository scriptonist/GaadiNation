import unittest
import math,random
from app import app
from app import models
from pymongo import MongoClient
import time


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
        self.collection = models.init_db()
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

    def test_search_by_carname_returns_correct_results(self):
        """ Check if the models.py gives correct result on query """
        
        # -------------------Get a search String--------- #
        # a document is returned as a cursor from the get_random_document method
        # It is iterated to find the carname and stored to search_string
        search_string = [string['carname'] for string in self.get_random_document()][0]
        # ----------------------------------------------- #

        # To check if all parts of the search string will be matched 
        # the string is split with respect to spaces and checked for match
        search_string_list = search_string.split()
        for query in search_string_list:
            result = models.find_by_car_name(query)
            carname_list = [entry['carname'] for entry in result]
            self.assertIn(str(search_string), carname_list)
            self.assertNotIn(str(search_string)+'x', carname_list)

    def test_fetch_car_details_of_a_car_give_correct_results(self):
        """
        Check if the models.py get_details_of_car(carname) return
         correct Results
        """
        # Get a Carname from the DB
        carname = [document for document in self.get_random_document()][0]['carname']
        result = models.get_details_of_car(carname)
        # Check if returned value is a dictionary
        self.assertEqual(True,isinstance(result,dict))
        # Check if the query returned the correct car results
        self.assertEqual(carname,result['carname'])
        # Check id the query evaluates to wrong
        self.assertNotEqual(carname+'x',result['carname'])



if __name__ == "__main__":
    unittest.main()
