#!/usr/bin/python3

from models.review import Review
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
