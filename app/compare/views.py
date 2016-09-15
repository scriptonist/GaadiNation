from flask import Blueprint, render_template, request
from app.models import getcars, getcardetails, getmanufacturer
import json

compare = Blueprint("compare", __name__, url_prefix='/compare')


@compare.route('/')
def compare_index():
    return render_template("compare/compare_index.html", manu=getmanufacturer())


@compare.route('/result/<brand>', methods=['GET'])
def carlist(brand):
    cars = getcars(brand)
    return json.dumps(cars)


@compare.route('/compare_display', methods=['POST'])
def compare_display():
    number = count = 0
    details1 = getcardetails(request.form['list1'])
    details2 = getcardetails(request.form['list2'])
    details3 = getcardetails(request.form['list3'])
    details4 = getcardetails(request.form['list4'])
    cars = [details1, details2, details3, details4]
    for k in cars:
        if len(k) > 0:
            count = count + 1
    if count == 1:
        number = 37
    elif count == 2:
        number = 17
    elif count == 3:
        number = 6
    else:
        number = 0
    return render_template("compare/compare_result1.html", cars=cars, number=number)


@compare.route('/compare_display/<carlist>', methods=['GET'])
def compare_display2(carlist=None):
    carlist = carlist.split(",")
    print(carlist)
    details = []
    for car in carlist:
        details.append(getcardetails(car))
    count = len(carlist)
    if count == 1:
        number = 37
    elif count == 2:
        number = 17
    elif count == 3:
        number = 6
    else:
        number = 0
    return render_template("compare/compare_result1.html",cars=details,number=number)
