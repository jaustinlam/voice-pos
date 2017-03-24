from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from flask import session
import random
import string
# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.client import FlowExchangeError
# import httplib2
import json
from flask import make_response
import requests
import login_helpers
import voice

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login_page():

	if request.method == 'POST':
		current_user = request.form.values()
		current_user_pass = 0
		for x in current_user:
			current_user_pass = x
		user = login_helpers.getUserByPasscode(int(current_user_pass))
		print(user)
		if user != None:
			session['username'] = user.name
			return redirect(url_for('items_page'))
		else:
			flash("Sorry User not found, please try again.")
			return render_template('login.html')
	else:
		return render_template('login.html')

items_array = []
@app.route('/items', methods=['GET', 'POST'])
def items_page():
	new_item = voice.return_text()
	if request.method == 'POST':
		new_item = voice.return_text()
		items_array.append(new_item)
		print(new_item)
		return render_template('items.html', items = items_array)
	else:
		return render_template('items.html')

@app.route('/checkout')
def checkout_page():
	return render_template('checkout.html')

@app.route('/receipt')
def receipt_page():
	return render_template('receipt.html')
	# TO DO
	# show receipt with transaction information
	# maybe text or email the receipt





# Run app
if __name__ == '__main__':
    app.secret_key = "123456789"  # If testing enter your own secret key
    app.debug = True
    app.run(host='0.0.0.0', port=7000)
