from flask import Blueprint,render_template

recomendation = Blueprint("recomendation", __name__, url_prefix='/recomendation')

@recomendation.route('/questions')
def recomendation_steps():
    return render_template("recomendation/find.html")

@recomendation.route('/result')
def recomendation_result():
    return render_template("recomendation/findresult.html")