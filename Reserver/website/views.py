from flask import Blueprint, redirect, render_template, url_for, request

from . import db

views = Blueprint('views', __name__)
#TODO: Make a homepage
@views.route('/')
def index():
    #put the homepage here
