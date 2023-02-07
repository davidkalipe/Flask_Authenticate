from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, redirect, url_for, request, flash
# from flask_bcrypt import generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from project.models import User
from project import db

auth = Blueprint('auth', __name__)

@auth.route('/home')
def home():
    return render_template('home.html')

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/sign')
def sign():
    return render_template('sign.html')


@auth.route('/success')
def success():
    return render_template('success.html')


@auth.route('/success1')
def success1():
    return render_template('success1.html')


@auth.route('/sign', methods=['POST'])
def sign_post():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')
    users = User.query.filter_by(email=email).first()

    if users:
        flash('Email address already exists')
        return redirect(url_for('auth.sign'))

    new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password))

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    users = User.query.filter_by(email=email).first()
    if users is None or not check_password_hash(users.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    return redirect(url_for('auth.success1'))


