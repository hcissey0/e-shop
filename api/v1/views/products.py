#!/usr/bin/python3

from models.product import Product
from models import storage
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def products_list():
    product_list = []
    for i in Product.all():
        product_list.append(i.to_dict())
    return jsonify(product_list)

@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id):
    product = Product.query(id=product_id)
    if not product:
        abort(404)
    return jsonify(product.to_dict())
