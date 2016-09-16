from flask import Blueprint, render_template, request, jsonify
from app.models import filter_by_many_values_perfect
import json,ast

catalog = Blueprint("catalog", __name__, url_prefix='/catalog')

@catalog.route('/', defaults={'filters': None},methods=["POST","GET"])
@catalog.route('/<filters>', methods=["POST", "GET"])
def compare_index(filters=None):
    if request.method == "GET" and filters is None:
        content = filter_by_many_values_perfect()
        return render_template("catalog/catalog_index.html", result=content)
    else:
        filters = list(ast.literal_eval(filters))
        print(filters)
        new_content = filter_by_many_values_perfect(filters)
        return render_template("catalog/catalog_index.html",result=new_content)
        