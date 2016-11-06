from flask import session
from .models import Product

def set_cart_session():
    if "cart" not in session:
        session.setdefault('cart', {})
    return True

def clear_cart_session():
    if "cart" in session:
        del session["cart"]
    return True


def get_order_details():
    total_price = 0
    product_ids = session["cart"].keys()
    if product_ids:
        products = Product.query.with_entities(Product.id, Product.price).filter(Product.id.in_(map(int, product_ids))).all()
    else:
        return None
    for product in products:
        total_price += product.price * session["cart"].get(str(product.id))
    return total_price
