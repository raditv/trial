import odoorpc
from flask import url_for, current_app

class Customer(object):
	def get_data(self,user,password):
		odoo = odoorpc.ODOO(current_app.config['ODOO_HOST'], port=8069)
		odoo.login('devel', user, password)
		if 'res.partner' in odoo.env:
			Customer = odoo.env['res.partner']
			customer_ids = Customer.search([('customer','=',True),('company_type','=','person')])
			customers = dict()
			for customer in Customer.browse(customer_ids):
				customers[customer.id]= {'Nama': customer.name, 'Alamat': customer.street, 'Telp': customer.phone, 'Email': customer.email, 'Credit': customer.credit, 'Debit': customer.debit}
		return customers

class Product(object):
	def get_data(self,user,password):
		odoo = odoorpc.ODOO(current_app.config['ODOO_HOST'], port=8069)
		odoo.login('devel', user, password)
		if 'product.template' in odoo.env:
			Product = odoo.env['product.template']
			product_ids = Product.search([])
			products = dict()
			for product in Product.browse(product_ids):
				products[product.id]= {'Nama': product.name, 'Kategori': product.categ_id, 'Kode': product.default_code, 'Harga': product.list_price}
		return products