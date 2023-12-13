#!/usr/bin/python3
"""This is the views for the shops"""

from web_flask.views import main
from models import storage
from models.shop import Shop
from flask_login import login_required, current_user
from flask import render_template, abort, redirect, request,url_for, flash
import uuid


@main.route("/shops", strict_slashes=False)
def shops_list():
    return render_template('shop-list.html', shops=Shop.all(), cache_id=uuid.uuid4())


@main.route('/shops/<shop_id>', strict_slashes=False)
def shop(shop_id):
    shop = Shop.query(id=shop_id)
    if shop:
        return render_template('shop.html', shop=shop, cache_id=uuid.uuid4())
    abort(404)

@main.route('/edit-shop/<shop_id>', methods=['POST'], strict_slashes=False)
def edit_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    args = request.form.to_dict()
    shop.update(**args)
    shop.save()
    flash('Shop updated successfully', 'success')
    return redirect(url_for('main.manage_shop', shop_id=shop_id))

@main.route('/manage-shop/<shop_id>', strict_slashes=False)
def manage_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    return render_template('manage-shop.html', shop=shop, cache_id=uuid.uuid4())

@main.route('/delete-shop/<shop_id>', strict_slashes=False)
def delete_shop(shop_id):
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    # shop.user.shops.remove(shop)
    storage.delete(shop)
    storage.save()
    flash('Shop deleted successfully', 'success')
    return redirect(url_for('main.user_shops'))

@main.route('/create-shop', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def create_shop():
    if request.method == 'POST':
        shop_name = request.form.get('name')
        about = request.form.get('about')

        shop = Shop(
            name=shop_name,
            user_id=current_user.id,
            about=about
        )
        shop.save()
        current_user.shops.append(shop)
        current_user.save()
        flash('Shop created successfully', 'success')
        return redirect(url_for('main.user_shops'))
    return render_template('create-shop.html', cache_id=uuid.uuid4())

