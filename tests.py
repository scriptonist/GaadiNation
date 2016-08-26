import unittest
import Math
from app import app
from app import models
from pymongo import MongoClient


class test_app(unittest.TestCase):
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

        # Initialise collection variable with app config
        self.collection = models.initDb()

        # Insert the data in original database to test_database
        self.collection.insert(cars.find())

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
        R = Math.floor(Math.random() * n)
        # ----------------------------------------------- #
        document = self.collection.find().limit(1).skip(R)
        return document

    def test_returns_correct_result(self):
        pass

if __name__ == "__main__":
    unittest.main()
