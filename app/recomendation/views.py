from flask import Blueprint, render_template, request

recomendation = Blueprint("recomendation", __name__,
                          url_prefix='/recomendation')


@recomendation.route('/', methods=['post', 'get'])
def recomendation_steps():
    return render_template("recomendation/find.html")


@recomendation.route('/result', methods=["POST", "GET"])
def recomendation_result():
    form = request.form
    choices = {}
    if request.method == "POST":
        for key in form.keys():
            k = key.split(":")
            choices[k[0]] = k[1]
        print(choices)
        return render_template("recomendation/findresult.html", form=request.form)
    else:
        return render_template('404.html')
