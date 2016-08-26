from flask import Blueprint, render_template, redirect, request
from .forms import MyForm
from app.models import find_by_car_name

submit = Blueprint("views", __name__, url_prefix='/search')


@submit.route("/submit", methods=["POST", "GET"])
def submit_form():
    form = MyForm()
    content = None
    if form.validate_on_submit():
        content = find_by_car_name(request.form['name'])
    return render_template('search/form.html', form=form, result=content)


