from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        print "Product id:{} name: {}".format(self.id, self.name)
 
    def get_id(self):
        return unicode(self.id)
