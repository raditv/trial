import odoorpc
from flask import url_for, current_app

class Customer(object):
	def get_data(self,user,password):
		odoo = odoorpc.ODOO(current_app.config['ODOO_HOST'], port=80)
		odoo.login('devel', user, password)
		#user = odoo.env.user
		#user_data = odoo.execute('res.users', 'read', [user.id])
		if 'res.partner' in odoo.env:
			Customer = odoo.env['res.partner']
			customer_ids = Customer.search([('customer','=',True),('company_type','=','person')])
			customers = dict()
			for customer in Customer.browse(customer_ids):
				customers[customer.id]= {'Nama': customer.name, 'Alamat': customer.street, 'Telp': customer.phone, 'Email': customer.email, 'Credit': customer.credit, 'Debit': customer.debit}
		return customers