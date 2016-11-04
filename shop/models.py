from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    picture_name = db.Column(db.String(32), nullable=False)
    
    def __init__(self, name, price, picture_name):
        self.name = name
        self.price = price
        self.picture_name = picture_name

    def __repr__(self):
        print "Product id:{} name: {}".format(self.id, self.name)
 
    def get_id(self):
        return unicode(self.id)
