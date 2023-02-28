#!/usr/bin/python3

from models.category import Category
from models import storage
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def categories_list():
    category_list = []
    for i in Category.all():
        category_list.append(i.to_dict())
    return jsonify(category_list)

@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    category = Category.query(id=category_id)
    if not category:
        abort(404)
    return jsonify(category.to_dict())
