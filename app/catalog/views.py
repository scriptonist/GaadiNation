from flask import Blueprint, render_template
from app.models import filter_by_many_values_perfect

catalog = Blueprint("catalog", __name__, url_prefix='/catalog')


@catalog.route('/')
def compare_index():
    content = filter_by_many_values_perfect()
    return render_template("catalog/catalog_index.html",result=content)



