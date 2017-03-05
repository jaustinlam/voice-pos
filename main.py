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



app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')



# Run app
if __name__ == '__main__':
    app.secret_key = 123456789  # If testing enter your own secret key
    app.debug = True
    app.run(host='0.0.0.0', port=7000)
