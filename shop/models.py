from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    picture_name = db.Column(db.String(32), nullable=False)
    amount_on_stock = db.Column(db.Integer, default=0)

    
    def __init__(self, name, price, picture_name, amount_on_stock):
        self.name = name
        self.price = price
        self.picture_name = picture_name
        self.amount_on_stock = amount_on_stock

    def __repr__(self):
        print "Product id:{} name: {}".format(self.id, self.name)
 
    def is_available(self):
        return True if self.amount_on_stock else False
