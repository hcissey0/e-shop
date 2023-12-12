#!/usr/bin/python3

from models.shop import Shop
from models.user import User
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


@app_views.route('/users/<user_id>/shops', methods=['GET'], strict_slashes=False)
def get_user_shops(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    shops_list = []
    for shop in user.shops:
        shops_list.append(shop.to_dict())
    return jsonify(shops_list)

@app_views.route('/shops/<shop_id>', methods=['DELETE'], strict_slashes=False)
def delete_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    storage.delete(shop)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/shops', methods=['POST'], strict_slashes=False)
def create_a_shop():
    if not request.is_json:
        abort(400, description='Not a JSON')

    if 'name' not in request.get_json():
        abort(400, description='Missing name')
    if 'user_id' not in request.get_json():
        abort(400, description='Missing user_id')
    shop = Shop(**request.get_json())
    return make_response(jsonify(shop.to_dict()), 201)

@app_views.route('/shops/<shop_id>', methods=['PUT'], strict_slashes=False)
def update_a_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    if not request.is_json:
        abort(400, description='Not a JSON')
    shop.update(**request.get_json())
    shop.save()
    return make_response(jsonify(shop.to_dict()), 200)
    