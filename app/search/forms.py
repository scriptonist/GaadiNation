from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(Form):
    name = StringField('search',validators=[DataRequired()],render_kw={"placeholder": "Type a car name"})

