from flask import Blueprint,render_template

recomendation = Blueprint("recomendation", __name__, url_prefix='/recomendation')

@recomendation.route('/')
def index_recomendation():
    return render_template("recomendation/index.html")

@recomendation.route('/steps')
def steps(step=None):
    if step is None:
        return render_template("recomendation/step1.html")
    elif step == 2:
        return render_template("recomendation/step2.html")
    elif step == 3:
        return render_template("recomendation/step3.html")