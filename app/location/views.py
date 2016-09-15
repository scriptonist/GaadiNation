from flask import Blueprint, render_template,request
from urllib.request import urlopen
from urllib.parse import urlencode
import json

location = Blueprint("location", __name__, url_prefix='/locate')


googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(query, from_sensor=False):
    query = query.encode('utf-8')
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urlencode(params)
    json_response = urlopen(url)
    response = json.loads(json_response.read().decode('utf-8'))
    if response['results']:
        loc = response['results'][0]['geometry']['location']
        latitude, longitude = loc['lat'], loc['lng']
    else:
        latitude, longitude = None, None
    return latitude, longitude


@location.route('/',methods=["post","get"])
def locate_index():
    if request.method == "GET":
        return render_template('location/location.html',lat=9.5916,lon=76.5222)
    else:
        query = request.form['searchTextField']
        l = get_coordinates(query)
        return render_template('location/location.html',lat=l[0],lon=l[1])





