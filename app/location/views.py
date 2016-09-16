from flask import Blueprint, render_template,request
from urllib.request import urlopen
from urllib.parse import urlencode
import json

location = Blueprint("location", __name__, url_prefix='/locate')
@location.route('/', defaults={'lat':9.5916,'lon':76.5222})
@location.route('/<float:lat>/<float:lon>',methods=["post", "get"])
def locate_index(lat,lon):
    if request.method == "GET":
        return render_template('location/location.html',lat=lat,lon=lon)
