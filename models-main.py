#!/usr/bin/python3
"""This is used to test the models created"""

from models.base_model import BaseModel
from models.user import User
from models.shop import Shop
from models.product import Product
from models.category import Category
from models.review import Review

from models import storage

import uuid
id = str(uuid.uuid4())
bm = BaseModel(id=id)

# print("\n\n-----BaseModel-----\n\n")

# print(bm.to_dict())
# print(id)


# print("\n\n------User Model-----\n\n")

# id = str(uuid.uuid4())
# det = {
# 'first_name' : "kofi",
# 'last_name' : "anan",
# 'username': 'kofianan',
# 'email' : "a@b.c",
# 'password' : "pass"
# }
# usr = User(**det)

# print(usr)

# print('\n\n-----Shop Model-----\n\n')

# det = {
#     'name': 'my shop',
#     # 'user_id': usr.id
# }

# shop = Shop(**det)
# usr.shops.append(shop)

# print(shop)
# print(shop.user)
# print(usr.shops[0])

# print("\n\n-----Product Model-----\n\n")

# det = {
#     'name': 'Book',
#     'price': 29.99,
#     # 'shop_id': shop.id
# }

# prod = Product(**det)
# print(prod)

# shop.products.append(prod)
# print(prod.shop.user)

# print(shop.products)

# print("\n\n-----Tag Model----\n\n")

# det = {
#     'name': 'Books'
# }

# category = Category(**det)
# category.products.append(prod)
# print(category.products[0])
# usr.save()
# shop.save()
# prod.save()
# category.save()

# storage.save()

# print("\n\n")

for i in storage.all('User').values():
    print(i)

print("\n\n-----This is the query test======\n\n")

print("\n\n-----Tag Model----\n\n")

for i in User.all():
    print(i)

print("\n\n-----User Model----\n\n")
[print(i) for i in User.all()]
print("\n\n-----Shop Model----\n\n")
[print(i) for i in Shop.all()]
print("\n\n-----Category Model----\n\n")
[print(i) for i in Category.all()]
print("\n\n-----Products Model----\n\n")
[print(i) for i in Product.all()]
print("\n\n-----Review Model----\n\n")
[print(i) for i in Review.all()]


print(User.query(email='hushedtremendous@eshop.com'))

print(Category.query(name='Books'))

print(User.all())

print(Product.all()[0])