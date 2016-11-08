import os
from flask_script import Manager
from shop import app

manager = Manager(app)


@manager.command
def init_db():
    '''Initialise database. Create schema'''
    from shop import app, db
    with app.app_context():
        db.create_all()


@manager.command
def add_records_for_test():
    '''Add few test records to table Product '''
    from shop import app, db
    from shop.models import Product
    with app.app_context():
        products = [Product('Milk', 10, "/static/milk.jpg", 10)]
        products.append(Product('Super water', 500, "/static/water.jpg", 3))
        products.append(Product('Beef meat 1kg', 70, "/static/meat.jpg", 7))
        products.append(Product('Candy', 7, "/static/meat.jpg", 50))
        products.append(Product('Orange 1kg', 20, "/static/meat.jpg", 24))
        products.append(Product('Apple 1kg', 14, "/static/meat.jpg", 20))
        products.append(Product('Power bar', 25, "/static/meat.jpg", 10))

        for product in products:
            db.session.add(product)

        db.session.commit()

@manager.command
def clean_tables():
    ''' Drop all tadbles in DB '''
    from shop import app, db
    from shop.models import Product
    with app.app_context():
        db.drop_all()
        db.session.commit()

@manager.command
def run_app():
    '''Initiate DB and run application '''
    clean_tables()
    init_db()
    add_records_for_test()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    manager.run()
