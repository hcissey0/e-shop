#!/usr/bin/python3

from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/accounts/')

from web_flask.views.auth_views import *

main = Blueprint('main', __name__)

from web_flask.views.main_views import *
from web_flask.views.shops import *
from web_flask.views.users import *
from web_flask.views.categories import *
from web_flask.views.products import *
