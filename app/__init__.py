from flask import Flask,render_template

app = Flask(__name__)
app.config.from_pyfile('configModule.cfg')

from .search.views import search

app.register_blueprint(search)


@app.route("/")
def index():
    return render_template("index.html",title="home")

@app.errorhandler(404)
def handle_404_error():
    return render_template('404.html'),404


@app.route("/test")
def test_components():
    return render_template("test.html",title="test")

