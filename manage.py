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
        product1 = Product('Milk', 10)
        product2 = Product('Super water', 500)
        product3 = Product('Beef meat', 70)

        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.commit()

@manager.command
def run_app():
    '''Initiate DB and run application '''
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    manager.run()