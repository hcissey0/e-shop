#!/usr/bin/python3
"""This is the flask app"""

from flask import Flask, render_template, abort

from models import storage
from models.user import User
from models.product import Product
from models.shop import Shop
from models.category import Category
from models.review import Review
import uuid


app = Flask(__name__)


context = {
    'shops': Shop.all(),
    'products': Product.all(),
    'users': User.all(),
    'categories': Category.all(),
    'reviews': Review.all(),
    'featured_products': sorted(Product.all(), key=lambda x: x.created_at)[:9],
    'cache_id': uuid.uuid4()
}
shops = Shop.all()
products= Product.all()
users= User.all()
categories= Category.all()
reviews= Review.all()
featured_products= sorted(Product.all(), key=lambda x: x.created_at)[:9]
cache_id= uuid.uuid4()

@app.teardown_appcontext
def teardown(error):
    storage.close()

@app.errorhandler(404)
def errorhandlerr(error):
    return render_template('error.html')

@app.route("/", strict_slashes=False)
def home():
    categories = Category.all()
    shops = Shop.all()
    featured_products = Product.all()[:9]
    return render_template('home.html',shops = Shop.all(),
products= Product.all(),
users= User.all(),
categories= Category.all(),
reviews= Review.all(),
featured_products= sorted(Product.all(), key=lambda x: x.created_at)[:9],
cache_id= uuid.uuid4())


@app.route("/users", strict_slashes=False)
def users_list():
    users = storage.all(User).values()
    return render_template('users-list.html', context=context)


@app.route("/products", strict_slashes=False)
def products_list():
    products = storage.all(Product).values()
    return render_template('products-list.html', context=context)


@app.route("/shops", strict_slashes=False)
def shops_list():
    shops = storage.all(Shop).values()
    return render_template('shop-list.html', shops = Shop.all(),
products= Product.all(),
users= User.all(),
categories= Category.all(),
reviews= Review.all(),
featured_products= sorted(Product.all(), key=lambda x: x.created_at)[:9],
cache_id= uuid.uuid4())

@app.route('/shops/<shop_id>', strict_slashes=False)
def shop(shop_id):
    shop = Shop.query(id=shop_id)
    if shop:
        return render_template('shop.html', shop=shop)
    abort(404)
    


@app.route("/tags", strict_slashes=False)
def tags_list():
    categories = storage.all(Category).values()
    return render_template('tags-list.html', context=context)


@app.route('/all', strict_slashes=False)
def all():
    users = storage.all(User).values()
    return render_template('all.html',shops = Shop.all(),
products= Product.all(),
users= User.all(),
categories= Category.all(),
reviews= Review.all(),
featured_products= sorted(Product.all(), key=lambda x: x.created_at)[:9],
cache_id= uuid.uuid4())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
