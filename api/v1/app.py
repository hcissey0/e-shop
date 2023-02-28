#!/usr/bin/python3

from flask import Flask, make_response, jsonify, request
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_database(error):
    storage.close()

@app.errorhandler(404)
def error_404(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001', debug=True)
