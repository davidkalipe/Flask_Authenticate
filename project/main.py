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
    return render_template('success.html')
