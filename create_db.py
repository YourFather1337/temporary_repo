from flask import Flask
from models import Mobile, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mobile.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        gadget1 = Mobile(model='IPhone 16 pro max', price=88000, color='Desert Gold', battery='4000Mah')
        gadget2 = Mobile(model='Iphone 11', price=10000000, color='Black Edition', battery='-1000Mah')
        gadget3 = Mobile(model='Iphone 12', price=2, color='White Edition', battery='1000Mah')
        gadget4 = Mobile(model='Iphone 14 Pro', price=10, color='Black Edition', battery='-3600Mah')
        db.session.add_all([gadget1, gadget2, gadget3, gadget4])
        db.session.commit()

       