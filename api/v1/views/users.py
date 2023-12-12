#!/usr/bin/python3

from models.user import User
from models import storage
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users_list():
    user_list = []
    for i in User.all():
        user_list.append(i.to_dict())
    return jsonify(user_list)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    if not request.is_json:
        abort(400, description='Not a JSON')
    if 'email' not in request.get_json():
        abort(400, description='Missing E-mail')
    if 'password' not in request.get_json():
        abort(400, description='Missing password')
    if 'username' not in request.get_json():
        abort(400, description='Missing username')

    data = request.get_json()
    user = User(**data)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_a_user(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    if not request.is_json:
        abort(400, description='Not a JSON')
    user.update(**request.get_json())
    user.save()
    return make_response(user.to_dict(), 200)
