from flask import render_template, session, jsonify, request
from . import app
from .models import Product
from .helper import cart_session

@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():

    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/shopping_cart', methods=['GET','POST'])
def shopping_cart():
    cart_session()
    
    if request.method == "POST":
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        session["cart"][str(id)] = qty #set new amount

    products = Product.query.filter(Product.id.in_(session["cart"])).all()
    product_amount = dict(map(lambda p: (p.id, session["cart"].get(str(p.id))), products))

    return render_template('shopping_cart.html', products=products, product_amount=product_amount)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        id = int(request.form['id'])
        qty = int(request.form['qty'])

        cart_session()
        session["cart"][str(id)] = session["cart"].get(str(id), 0) + qty

        return jsonify(status='ok')