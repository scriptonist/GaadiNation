from flask import Blueprint, render_template,request,jsonify
from app.models import filter_by_many_values_perfect
import json

catalog = Blueprint("catalog", __name__, url_prefix='/catalog')


@catalog.route('/',methods=["post","get"])
def compare_index():
    if request.method == "GET":
        content = filter_by_many_values_perfect()
        return render_template("catalog/catalog_index.html",result=content)
    else:

        filters = json.loads(request.data.decode('utf-8'))
        filters['brand'] = {"$in":filters['brand']}
        filters = [filters]
        new_content = filter_by_many_values_perfect(filters)
        return "hello"



