from flask_login import login_required, current_user
from flask import Blueprint, render_template, Flask
from project import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/success')
@login_required
def success():
    return render_template('success.html', lastname=current_user.lastname)

@main.route('/success1')
@login_required
def success1():
    return render_template('success1.html', lastname=current_user.lastname)
