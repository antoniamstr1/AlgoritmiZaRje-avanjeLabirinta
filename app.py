from views import views
from flask import Flask
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

if __name__ == '__main__':
    # debud automatski refresha aplikaciju
    app.run(debug=True)
