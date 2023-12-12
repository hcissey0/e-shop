#!/usr/bin/python3

from web_flask.views import main
from flask import render_template, abort, redirect
from models import storage
from models.user import User
from models.product import Product
from models.shop import Shop
from models.category import Category
from models.review import Review
import uuid
from flask_login import login_required, current_user


# This is the home route
@main.route("/", strict_slashes=False)
def home():
    return render_template('home.html', user=current_user,
                           shops = Shop.all(),
products= Product.all(),
users= User.all(),
categories= Category.all(),
reviews= Review.all(),
featured_products= sorted(Product.all(), key=lambda x: x.created_at)[:9],
cache_id= uuid.uuid4())

