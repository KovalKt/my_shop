from flask import request, url_for, session, redirect
from flask import jsonify, render_template, flash
from . import app, db
from .models import Product
from .forms import PaymentSettingsForm
from .helper import set_cart_session, clear_cart_session, get_order_details
from .payment_settings import PayPal, Privat24, Liqpay


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
    set_cart_session()
    
    if request.method == "POST":
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        session["cart"][str(id)] = qty #set new amount

    form = PaymentSettingsForm()

    products = Product.query.filter(Product.id.in_(session["cart"])).all()

    product_amount = dict()
    for product in products:

        if session["cart"].get(str(product.id)) > product.amount_on_stock:
            session["cart"][str(product.id)] = product.amount_on_stock
            product_amount[product.id] = product.amount_on_stock
        else:
            product_amount[product.id] = session["cart"].get(str(product.id))

    return render_template('shopping_cart.html', 
        products=products, 
        product_amount=product_amount,
        form=form
    )


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        id = int(request.form['id'])
        qty = int(request.form['qty'])

        set_cart_session()
        session["cart"][str(id)] = session["cart"].get(str(id), 0) + qty

        return jsonify(status='ok')

@app.route('/remove_item', methods=['POST'])
def remove_item():
    if request.method == 'POST':
        id = int(request.form['id'])

        set_cart_session()
        del session["cart"][str(id)]
        return jsonify(status='ok')


@app.route('/pay-now', methods=['POST'])
def pay_now():
    form = PaymentSettingsForm()
    system = eval(request.form['payment_system'])()
    total_price = get_order_details()

    products_ids = session["cart"].keys()
    products_in_cart = Product.query.filter(Product.id.in_(products_ids)).all()

    for product in products_in_cart:
        product.amount_on_stock -= session["cart"][str(product.id)]

    db.session.commit()

    flash(system.pay(total_price, "UAH"))

    clear_cart_session()

    return redirect(url_for('index'))   
