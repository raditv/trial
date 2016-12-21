from flask import request
from . import api
from ..models import Product
from ..decorators import json


@api.route('/products/', methods=['GET'])
@json
def get_products():
    return Product().get_data(request.headers['username'],request.headers['password'])

@api.route('/products/', methods=['POST'])
@json
def new_product():
    return {}, 201, {'Location': product.get_url()}
