#!/usr/bin/python3

from web_flask.views import main
from flask import render_template, abort
from models.category import Category
import uuid


@main.route('/categories', strict_slashes=False)
def categories_list():
    categories = Category.all()
    return render_template('categories.html', categories=categories, cache_id=uuid.uuid4())


@main.route('/categories/<category_id>', strict_slashes=False)
def list_products_by_category(category_id):
    category = Category.query(id=category_id)
    if not category:
        abort(404)
    return render_template('category-products.html', category=category, cache_id=uuid.uuid4())
