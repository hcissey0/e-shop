#!/usr/bin/python3

from models.product import Product
from models.shop import Shop
from models.category import Category
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

@app_views.route('/shops/<shop_id>/products', methods=['GET'],strict_slashes=False)
def get_products_by_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    prod_list = []
    for prod in shop.products:
        prod_list.append(prod.to_dict())
    return jsonify(prod_list)

@app_views.route('/categories/<category_id>/products', methods=['GET'], strict_slashes=False)
def get_products_by_category(category_id):
    cat = Category.query(id=category_id)
    if not cat:
        abort(404)
    prod_list = []
    for prod in cat.products:
        prod_list.append(prod.to_dict())
    return jsonify(prod_list)
