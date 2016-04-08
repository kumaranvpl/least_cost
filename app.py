from flask import Flask, render_template
from route_functions import config, add_state, add_product, add_seller, add_buyer, add_selling
from route_functions import find_all_states, find_all_products, find_all_sellers, find_all_buyers
from route_functions import calculate_least_cost


app = Flask(__name__)

app.secret_key = config['secret_key']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

selected_db = "mysql"
db_config = config["db"][selected_db]

app.config['SQLALCHEMY_DATABASE_URI'] = selected_db + "://" + db_config["username"] + ":" + db_config[
    "password"] + "@" + db_config["host"] + "/" + db_config["database"]

from models import db
db.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return "Oops... This page doesn't exists :p"


@app.route('/add_state')
def render_add_state():
    return render_template('add_state.html')


@app.route('/add_product')
def render_add_product():
    return render_template('add_product.html')


@app.route('/add_seller')
def render_add_seller():
    return render_template('add_seller.html', states_dict=find_all_states())


@app.route('/add_buyer')
def render_add_buyer():
    return render_template('add_buyer.html', states_dict=find_all_states())


@app.route('/add_selling')
def render_add_selling():
    return render_template('add_selling.html', sellers_dict=find_all_sellers(), products_dict=find_all_products())


@app.route('/calculate_least_cost')
def render_calculate_least_cost():
    return render_template('least_cost.html', buyers_dict=find_all_buyers(), products_dict=find_all_products())


app.add_url_rule('/state/add', view_func=add_state, methods=['GET', 'POST'])
app.add_url_rule('/product/add', view_func=add_product, methods=['GET', 'POST'])
app.add_url_rule('/seller/add', view_func=add_seller, methods=['GET', 'POST'])
app.add_url_rule('/buyer/add', view_func=add_buyer, methods=['GET', 'POST'])
app.add_url_rule('/selling/add', view_func=add_selling, methods=['GET', 'POST'])
app.add_url_rule('/calculate/least_cost', view_func=calculate_least_cost, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
