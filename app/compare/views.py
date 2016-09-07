from flask import Blueprint, render_template
from app.models import get_details_of_car

compare = Blueprint("compare", __name__, url_prefix='/compare')


@compare.route('/')
def compare_index():
    return render_template("compare/compare_index.html")


@compare.route('/list')
def compare_result():
    cars = [get_details_of_car("Tata ACE"), get_details_of_car("Maruti WagonR"), get_details_of_car(
        "Maruti Stingray"), get_details_of_car("Maruti Stingray")]
    number = int(12 / len(cars))
    return render_template("compare/compare_result.html", cars=cars, number=number)
