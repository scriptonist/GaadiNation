from flask import Blueprint,render_template

recomendation = Blueprint("recomendation", __name__, url_prefix='/recomendation')

@recomendation.route('/questions')
def recomendation_steps():
    return render_template("recomendation/find.html")

@recomendation.route('/result',methods=["POST","GET"])
def recomendation_result():
    if request.methos == "POST":
        return render_template("recomendation/findresult.html")
    else:
        return render_template('404.html')