from flask import Blueprint, render_template, request
from app.models import filter_by_many_values_perfect

recomendation = Blueprint("recomendation", __name__,
                          url_prefix='/recomendation')

"""
    This module recomends a car based on a users preferences
    if the following values are choosen for the preferences he 
    choose.
"""
budget = {"cheap": 1000000, "affordable": 3000000, "luxury": 3000000}
seatnumber = [2, 4, 5, 6, 7, 8]
use = {"daily": 18, "weekly": 15, "occasionaly": 10}


@recomendation.route('/', methods=['post', 'get'])
def recomendation_steps():
    return render_template("recomendation/find.html")


@recomendation.route('/result', methods=["POST", "GET"])
def recomendation_result():
    """
        This function will filter out cars from the db
        according to the preferences of the user
    """
    form = request.form
    choices = {}
    conditions = []
    if request.method == "POST":
        for key in form.keys():
            k = key.split(":")
            choices[k[0]] = k[1]
        if choices['budget'] == 'luxury':
            conditions.append({"start_price": {'$gte': budget['luxury']}})
            conditions.append({"SeatCapacity": {'$gte': seatnumber[seatnumber.index(int(choices['seatnumber']))]}})
        elif choices['budget'] == 'cheap':
            conditions.append({"start_price": {'$lte': budget['cheap']}})
            conditions.append({"SeatCapacity": {'$gte': seatnumber[seatnumber.index(int(choices['seatnumber']))]}})
            conditions.append({"Mileage": {'$gte': use[choices['use']]}})
        elif choices['budget'] == 'affordable':
            conditions.append({"start_price": {'$lte': budget['affordable']}})
            conditions.append({"start_price": {'$gt': budget['cheap']}})
            conditions.append({"SeatCapacity": {'$gte': seatnumber[seatnumber.index(int(choices['seatnumber']))]}})
            conditions.append({"Mileage": {'$gte': use[choices['use']]}})
        content=filter_by_many_values_perfect(conditions).limit(5)
        return render_template("recomendation/findresult.html", content=content)
    else:
        return render_template('404.html')
