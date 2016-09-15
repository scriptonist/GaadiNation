from flask import Blueprint,render_template,request

recomendation = Blueprint("recomendation", __name__, url_prefix='/recomendation')

@recomendation.route('/questions')
def recomendation_steps():
    return render_template("recomendation/find.html")

@recomendation.route('/result',methods=["POST","GET"])
def recomendation_result():
    if request.method == "POST":
        return render_template("recomendation/findresult.html",form=request.form)
    else:
        return render_template('404.html')