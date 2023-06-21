from flask import Blueprint, redirect, render_template, url_for, request

from . import db

views = Blueprint('views', __name__)
#TODO: Make a homepage
@views.route("/", methods=['GET','POST'])
def index():
    #put the homepage here
    #return render_template('index.html')
    return "<p>Hello, World!</p>"

@views.route("/home", methods=['GET','POST'])
def home():
    #put the homepage here
    return render_template('index.html')