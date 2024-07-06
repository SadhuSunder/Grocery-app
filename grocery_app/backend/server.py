from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import products_dao
import uom_dao
import orders_dao
import json
from sql_connection import get_sql_connection


app = Flask(__name__)
CORS(app)
connection = get_sql_connection()


@app.route('/get_products', methods=['GET'])
def get_products():
	products = products_dao.get_all_products(connection)
	response = jsonify(products)
	response.headers.add('Access-Control-Allow-Origin','*')
	return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
	response = uom_dao.get_uoms(connection)
	response = jsonify(response)
	response.headers.add('Access-Control-Allow-Origin','*')
	return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
	return_id = products_dao.delete_product(connection, request.form['product_id'])
	response = jsonify({
		'product_id': return_id
		})
	response.headers.add('Access-Control-Allow-Origin','*')
	return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
	response = orders_dao.get_all_orders(connection)
	response = jsonify(response)
	response.headers.add('Access-Control-Allow-Origin','*')
	return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
	requestPayload = json.loads(request.form['data'])
	order_id = orders_dao.insert_order(connection, requestPayload)
	response = jsonify({
		'order_id': order_id
		})
	response.headers.add('Access-Control-Allow-Origin','*')
	return response

@app.route('/insertProduct', methods=['POST'])
def insertProduct():
	requestPayload = json.loads(request.form['data'])
	product_id = products_dao.insert_new_product(connection, requestPayload)
	response = jsonify({
		'product_id': product_id
		})
	response.headers.add('Access-Control-Allow-Origin','*')
	return response

if __name__ == "__main__":
	print("Starting python Flask Server For Grocery Store MAnagement System")
	app.run(port=5000)
