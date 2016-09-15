from flask import Blueprint, render_template

location = Blueprint("location", __name__, url_prefix='/location')


@location.route('/',methods=["post","get"])
def locate_index():
    return render_template('location/sharelocation.html')
@location.route('/<int:lati>/<int:longi>',methods=["post","get"])
def locate():
    return render_template('location/location.html',lat=lati,lon=longi)



