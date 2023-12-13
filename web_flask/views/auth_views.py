#!/usr/bin/python3

from flask import render_template, request, url_for, flash, redirect
from web_flask.views import auth
from models.user import User
from flask_login import login_user, logout_user
import uuid


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query(email=email)
        if not user:
            flash('Invalid Email', 'danger')
            return redirect(url_for('auth.login'))
        if not user.check_password(password):
            flash('Wrong Password', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('login.html', cache_id=uuid.uuid4())


@auth.route('/logout', strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        name = first_name + " " + last_name
        username = request.form.get('username')
        if User.query(username=username):
            flash('Username already exists', category='warning')
            return redirect(url_for('auth.signup'))
        email = request.form.get('email')
        if User.query(email=email):
            flash('E-mail already exists', category='warning')
            return redirect(url_for('auth.signup'))
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Passwords do not match', category='danger')
            return redirect(url_for('auth.signup'))
        user = User(
            name=name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        # print('\n\n\n\nuser is created')
        user.save()
        # print('\n\n\n\nuser is saved')
        flash('Account created successfully', category='success')
        # print('\n\n\n\nflash message added')
        return redirect(url_for('auth.login'))


    return render_template('signup.html', cache_id=uuid.uuid4())
