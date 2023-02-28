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
