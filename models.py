from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mobile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(15), nullable=False )
    battery = db.Column(db.String(20), nullable=False)


