#!/usr/bin/python3

from flask import render_template, abort, request, flash, redirect, url_for
from models import storage
from models.product import Product
from models.category import Category
from models.shop import Shop
from web_flask.views import main
from flask_login import login_required, current_user

@main.route('/products/<product_id>', strict_slashes=False)
def product_details(product_id):
    product = Product.query(id=product_id)
    if not product:
        abort(404)
    return render_template('product-detail.html', product=product)


@main.route('/search', methods=['GET', 'POST'], strict_slashes=False)
def search_product():
    if request.method == 'POST':
        key = request.form.get('text')
        args = key.split()
        products = Product.all()
        search_list = []
        for p in products:
            for arg in args:
                if arg in p.name.lower():
                    search_list.append(p)

    return render_template('search.html', key=key, search_list=search_list)



@main.route('/create-product/<shop_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def create_product(shop_id):
    categories = Category.all()
    
    shop = Shop.query(id=shop_id)
    if not shop:
        abort(404)
    if request.method == 'POST':
        name = request.form.get('name')
        category_name = request.form.get('category_name')
        price = request.form.get('price')
        description = request.form.get('description')
        about = request.form.get('about')
        if category_name == 'Select':
            flash('Category is required', 'danger')
            return redirect(url_for('main.create_product', shop_id=shop_id))

        category = Category.query(name=category_name)
        product = Product(
            name=name,
            category_id = category.id,
            shop_id = shop.id,
            price=price,
            description=description,
            about=about
        )
        product.save()
        category.products.append(product)
        category.save()
        shop.products.append(product)
        shop.save()
        flash('Product created successfully', 'success')
        return redirect(url_for('main.manage_shop', shop_id=shop_id))
    
    return render_template('create-product.html', shop=shop, categories=categories)

@main.route('/delete-product/<product_id>', strict_slashes=False)
def delete_product(product_id):
    product = Product.query(id=product_id)
    if not product:
        abort(404)
    storage.delete(product)
    storage.save()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('main.manage_shop', shop_id=product.shop.id))