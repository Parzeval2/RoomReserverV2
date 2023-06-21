from flask import Blueprint, redirect, render_template, url_for, request
from .models import Group
from . import db

views = Blueprint('views', __name__)
#TODO: Make a homepage
@views.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@views.route("/SignIn", methods=['GET','POST'])
def SignIn():
    if request.method == 'POST':
        #pull the data from the form and pass into sql database
        id = request.form.get('id')
        CWID = request.form.get('CWID')
        size = request.form.get('size')
        email = request.form.get('email')
        #create new database object
        new_user = Group(id, CWID, size, email)
        #add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('views.status'))
@views.route("/status", methods=['GET','POST'])
def status():
    return render_template('status.html', )