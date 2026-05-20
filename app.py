from flask import Flask, render_template
from models import Mobile, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mobile.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/mobile')
def gadget():
    g_list = Mobile.query.all()
    return render_template('mobile.html', mobiles=g_list)

if __name__ =='__main__':
    app.run(debug=True)


