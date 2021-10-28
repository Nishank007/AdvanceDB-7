import os
import shutil
import csv
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
import requests

response = {
    "ip": None,
    "image": None,
    "mul_image": None,
    "show_image": None
}




# from operator import and_
# from os import abort
# from flask import Flask, render_template, request, redirect
# from flask.helpers import flash, url_for
# from sqlalchemy.sql.operators import op
# from sqlalchemy import func, distinct, select
# from werkzeug.utils import secure_filename
# from models import FilterModel, db
# import urllib.parse
# import csv
# import copy
# import os
# from datetime import datetime
# from math import radians, cos, sin, asin, sqrt
# import time
# import redis
# from flask_googlecharts import GoogleCharts
# from flask_googlecharts import BarChart


app = Flask(__name__)
port = int(os.getenv("PORT", 8000))
bootstrap = Bootstrap(app)

# conn = sqlite3.connect('names.db', check_same_thread=False)
# print("Opened database successfully")

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'

class NameForm(FlaskForm):
	name = StringField('Name', default="ABC")
	submit = SubmitField('Submit')

# ROUTES!
# @app.route('/',methods=['GET','POST'])
# def index():
#     return render_template('index.html', result={})

@app.route('/')
def index():

	global response
	ip = requests.get('https://checkip.amazonaws.com').text.strip()

	response["ip"] = ip
	response["image"] = "https://karan-adb-bucket.s3-us-west-2.amazonaws.com/aws.png"
	response["mul_image"] = "https://karan-adb-bucket.s3-us-west-2.amazonaws.com/mul.png"
	response["show_image"] = True

	return render_template('base.html', response=response)


ip = requests.get('https://checkip.amazonaws.com').text.strip()

@app.route('/help')
def help():
	text_list = []
	# Python Version
	text_list.append({
		'label':'Python Version',
		'value':str(sys.version)})
	# os.path.abspath(os.path.dirname(__file__))
	text_list.append({
		'label':'os.path.abspath(os.path.dirname(__file__))',
		'value':str(os.path.abspath(os.path.dirname(__file__)))
		})
	# OS Current Working Directory
	text_list.append({
		'label':'OS CWD',
		'value':str(os.getcwd())})
	# OS CWD Contents
	label = 'OS CWD Contents'
	value = ''
	text_list.append({
		'label':label,
		'value':value})
	return render_template('help.html',text_list=text_list,title='help')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')
