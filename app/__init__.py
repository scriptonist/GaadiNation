from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('configModule.cfg')

from .search.views import submit

app.register_blueprint(submit)


@app.route("/")
def index():
    return "Hello World"
