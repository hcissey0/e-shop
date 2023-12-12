#!/usr/bin/python3

from models import storage
from models.product import Product
from models.user import User
from models.category import Category
from web_flask.views import main
from flask_login import login_required, current_user
from flask import render_template, abort, redirect, request, flash, url_for
import uuid


@main.route('/user-shops', strict_slashes=False)
@login_required
def user_shops():
    return render_template('user-shops.html',
                           categories= Category.all()
                           )


@main.route('/user-cart', strict_slashes=False)
@login_required
def user_cart():
    return render_template('user-cart.html')


@main.route('/add-to-cart/<product_id>', strict_slashes=False)
@login_required
def add_to_cart(product_id):
    product = Product.query(id=product_id)
    if not product:
        abort(404)
    current_user.cart.products.append(product)
    current_user.cart.total += product.price
    current_user.cart.save()
    current_user.save()
    flash('Product added to cart successfully', 'success')
    
    return redirect(url_for('main.user_cart'))

@main.route('/remove-from-cart/<product_id>', strict_slashes=False)
def remove_from_cart(product_id):
    product = Product.query(id=product_id)
    if not product:
        abort(404)
    current_user.cart.total -= product.price
    storage.delete(product)
    storage.save()
    return redirect(url_for('main.user_cart'))

@main.route('/empty-cart', strict_slashes=False)
@login_required
def empty_cart():
    current_user.cart.products = []
    current_user.cart.total = 0.0
    current_user.cart.save()
    current_user.save()

    return redirect(url_for('main.user_cart'))
    
@main.route('/users/<user_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def user_details(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    if request.method == 'POST':
        if request.form.get('email') != user.email and User.query(email=request.form.get('email')) is not None:
            flash('Email alredy in use', 'danger')
            return redirect(url_for('main.home'))
        changes = request.form.to_dict(flat=True)
        if user.update(**changes) is None:
            flash(message="Error occured while making changes", category='danger')
            return redirect(url_for('main.home'))
        user.save()
        flash('Changes made successfully', 'success')
        return redirect(url_for('main.user_details', user_id=user_id))
    return render_template('user-details.html')


@main.route('/change-password/<user_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def change_password(user_id):
    user = User.query(id=user_id)
    if not user:
        abort(404)
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        if user.password != old_password:
            flash('Wrong password', 'danger')
            return redirect(url_for('main.change_password', user_id=user.id))
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        if new_password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('main.change_password', user_id=user.id))
        user.update(password=new_password)
        flash('Password changed successfully', 'success')
        return redirect(url_for('main.user_details', user_id=user.id))
    return render_template('change-password.html')

