from flask import Blueprint, render_template, redirect , request
from .forms import MyForm
from app.models import find_by_car_name

submit = Blueprint("views", __name__, url_prefix='/search',
                   template_folder="templates")


@submit.route("/submit", methods=["POST", "GET"])
def submit_form():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/result')
    return render_template('form.html', form=form)


@submit.route("/result", methods=['POST'])
def result():
    return render_template("results.html", result=find_by_car_name(
        request.form['name']))

