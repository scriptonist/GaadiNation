"""
    Initialize the Testing Class
"""

import flask_testing
import app as App


class testTest(flask_testing.TestCase):
    def create_app(self):
        app = App.app
        app.config['TESTING'] = True
        return app