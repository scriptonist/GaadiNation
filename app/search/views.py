from flask import Blueprint, render_template, redirect, request,jsonify
from app.models import find_by_car_name,get_details_of_car
import json

search = Blueprint("views", __name__, url_prefix='/search')

# The view function returning the results for a search query


@search.route("/", methods=["POST","GET"])
def search_form():
    if request.method == 'POST':
        content = find_by_car_name(request.form['search_query'])
        return render_template('search/results.html', result=content,
                               title="Search")
    else:
        return render_template('index.html')


# Ajax Request handler for the search box in landing     page


@search.route("/<query>", methods=["GET"])
def ajax_search_form(query=None):
    if query is not None:
        content = find_by_car_name(query)
        car_name_list = [{"carname":car['carname']} for car in content]
        return json.dumps(car_name_list)


@search.route("/getcardetails/<carname>",methods=["GET"])
def get_car_details_by_name(carname=None):
    if carname is not None:
        details = get_details_of_car(carname)
        return render_template("search/cardetails.html",details=details,found=True)
    else:
        return render_template("search/cardetails.html", found=False)
