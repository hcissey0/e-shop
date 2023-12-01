#!/usr/bin/python3
"""This is the flask app"""

from flask import Flask, render_template

from models import storage
from models.user import User
from models.product import Product
from models.shop import Shop
from models.category import Category
import uuid


app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    storage.close()


@app.route("/", strict_slashes=False)
def home():
    categories = Category.all()
    shops = Shop.all()
    featured_products = Product.all()[:9]
    return render_template('home.html',
                           categories=categories,
                           shops=shops,
                           featured_products=featured_products)


@app.route("/users", strict_slashes=False)
def users_list():
    users = storage.all(User).values()
    return render_template('users-list.html',
                           users=users,
                           cache_id=uuid.uuid4())


@app.route("/products", strict_slashes=False)
def products_list():
    products = storage.all(Product).values()
    return render_template('products-list.html',
                           products=products,
                           cache_id=uuid.uuid4())


@app.route("/shops", strict_slashes=False)
def shops_list():
    shops = storage.all(Shop).values()
    return render_template('shops-list.html',
                           shops=shops,
                           cache_id=uuid.uuid4())


@app.route("/tags", strict_slashes=False)
def tags_list():
    categories = storage.all(Category).values()
    return render_template('tags-list.html',
                           categories=categories,
                           cache_id=uuid.uuid4())


@app.route('/all', strict_slashes=False)
def all():
    users = storage.all(User).values()
    return render_template('all.html',
                           users=users,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
