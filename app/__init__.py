from flask import Flask,render_template

app = Flask(__name__)
app.config.from_pyfile('configModule.cfg')

from .search.views import submit

app.register_blueprint(submit)


@app.route("/")
def index():
    return render_template("index.html",title="home")
