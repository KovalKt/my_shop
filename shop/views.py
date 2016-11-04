from flask import render_template
from . import app
from .models import Product

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():

    products = Product.query.all()
    return render_template('index.html', products=products)