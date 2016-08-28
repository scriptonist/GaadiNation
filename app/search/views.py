from flask import Blueprint, render_template, redirect, request,jsonify
from app.models import find_by_car_name,get_details_of_car
import json

search = Blueprint("views", __name__, url_prefix='/search')

# The view function returning the results for a search query


@search.route("/", methods=["POST","GET"])
def search_form():
    """
     search handler for searching the database by carname
     the function expects a form containing an input field
     with name 'search_query' which can be accesed by
     request.form['search_query'] this function will return
     a template containing the results if it's a POST request
    """
    if request.method == 'POST':
        content = find_by_car_name(request.form['search_query'])
        return render_template('search/results.html', result=content,
                               title="Search")
    else:
        return render_template('index.html')


# Ajax Request handler for the search box in landing page


@search.route("/<query>", methods=["GET"])
def ajax_search_form(query=None):
    """
    ajax request handler function it takes urls like
    /search/<query>
    Eg. /search/Alto
    This will look up the database to find details of
    a car with name Alto
    it uses a function in models.py which returns a cursor
    the results from database it is encoded as JSON an returned to
    a JS function
    :param query:
    :return:JSON Data
    """
    if query is not None:
        content = find_by_car_name(query)
        car_name_list = [{"carname":car['carname']} for car in content]
        return json.dumps(car_name_list)


@search.route("/getcardetails/<carname>",methods=["GET"])
def get_car_details_by_name(carname=None):
    """
    Fetch all details avialable for a car from database
    expects a url like this
    /search/cardetails/Maruti Alto 800
    :param carname:
    :return: rendered template cardetails.html
    """
    if carname is not None:
        details = get_details_of_car(carname)
        return render_template("search/cardetails.html",details=details,found=True)
    else:
        return render_template("search/cardetails.html", found=False)
