#!/usr/bin/python3

from models.shop import Shop
from models import storage
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views


@app_views.route('/shops', methods=['GET'], strict_slashes=False)
def shops_list():
    shop_list = []
    for i in Shop.all():
        shop_list.append(i.to_dict())
    return jsonify(shop_list)

@app_views.route('/shops/<shop_id>', methods=['GET'], strict_slashes=False)
def get_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    return jsonify(shop.to_dict())
