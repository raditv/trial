from flask import request
from . import api
from ..decorators import json
from ..models import Customer

@api.route('/customers/', methods=['GET'])
@json
def get_customers():
    return Customer().get_data(request.headers['username'],request.headers['password'])

@api.route('/customers/<int:id>', methods=['GET'])
@json
def get_customer(id):
    return 'test one'

@api.route('/customers/', methods=['POST'])
@json
def new_customer():
    return {}, 201, {'Location': customer.get_url()}

@api.route('/customers/<int:id>', methods=['PUT'])
@json
def edit_customer(id):
    return {}
