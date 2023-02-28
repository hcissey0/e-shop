#!/usr/bin/python3

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1/')


from api.v1.views.users import *
from api.v1.views.categories import *
from api.v1.views.products import *
from api.v1.views.reviews import *
from api.v1.views.shops import *
