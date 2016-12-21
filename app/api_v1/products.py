from flask import request
from . import api
from ..models import Product
from ..decorators import json, paginate


@api.route('/products/', methods=['GET'])
@json
@paginate('products')
def get_products():
    return Product().get_data(request.headers['username'],request.headers['password'])

@api.route('/products/<int:id>', methods=['GET'])
@json
def get_product(id):
    return 'test one'

@api.route('/products/', methods=['POST'])
@json
def new_product():
    return {}, 201, {'Location': product.get_url()}

@api.route('/products/<int:id>', methods=['PUT'])
@json
def edit_product(id):
    return {}
