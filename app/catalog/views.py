from flask import Blueprint, render_template, request, jsonify
from app.models import filter_by_many_values_perfect
import json,ast

catalog = Blueprint("catalog", __name__, url_prefix='/catalog')

@catalog.route('/',methods=["POST","GET"])
def compare_index():
    if request.method == "GET":
        content = filter_by_many_values_perfect()
        return render_template("catalog/mycatalog.html", result=content)
    else:
        print(request.form)
        new_content = filter_by_many_values_perfect()
        return render_template("catalog/mycatalog.html",result=new_content)
