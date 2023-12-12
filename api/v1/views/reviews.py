#!/usr/bin/python3

from models.review import Review
from models.user import User
from models.product import Product
from models import storage
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def reviews_list():
    review_list = []
    for i in Review.all():
        review_list.append(i.to_dict())
    return jsonify(review_list)

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    review = Review.query(id=review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())

@app_views.route('/users/<user_id>/reviews', methods=['GET'], strict_slashes=False)
def get_user_reviews(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    reviews_list = []
    for review in user.reviews:
        reviews_list.append(review.to_dict())
    return jsonify(reviews_list)

@app_views.route('/products/<product_id>/reviews', methods=['GET'], strict_slashes=False)
def get_product_reviews(product_id):
    product = Product.query(id=product_id)
    if not product:
        abort(404)
    rev_list = []
    for rev in product.reviews:
        rev_list.append(rev.to_dict())
    return jsonify(rev_list)

@app_views.route('/users/<user_id>/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user_review(user_id, review_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    review = Review.query(id=review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/reviews',
                 methods=['POST'],strict_slashes=False)
def add_review():
    if not request.is_json:
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")
    if 'product_id' not in request.get_json():
        abort(400, "Missing product_id")
    if 'text' not in request.get_json():
        abort(400, "Missing text")
    review = Review(**request.get_json())
    review.save()

    return make_response(jsonify(review.to_dict()), 201)
    