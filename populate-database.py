#!/usr/bin/python3
"""This is used to add objects to the database"""

from models import storage
from models.user import User
from models.shop import Shop
from models.product import Product
from models.category import Category

import random
import random_name_generator.resources.name_generator as rng


cat_images = [
    'cat-1.jpg', 'cat-2.jpg', 'cat-3.jpg', 'cat-4.jpg'
]
shop_images = [
    'carousel-1.jpg', 'carousel-2.jpg','carousel-3.jpg'
]



def main():
    """This is to add objects to the database"""
    for i in range(5):
        first_name = rng.generate_name()[4:-5].capitalize()
        last_name = rng.generate_name()[4:-5].capitalize()
        user_name = first_name + " " + last_name
        username = (first_name + last_name).lower()
        image_name = "user-" + str(random.randint(1, 2)) + ".jpg"
        det = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'name': user_name,
            'email': (username) + "@eshop.com",
            'password': username,
            'image_name': image_name
        }
        user = User(**det)
        rand1 = random.randint(1, 2)
        
        for j in range(rand1):
            shop_name = rng.generate_name()[4:-5].capitalize()
            image_name = "vendor-" + str(random.randint(1, 8)) + ".jpg"
            shop = Shop(name=shop_name, image_name=image_name)
            user.shops.append(shop)
            rand2 = random.randint(1, 2)
            
            for k in range(rand2):
                name = rng.generate_name()[4:-5]
                image_name = "cat-" + str(random.randint(1, 4)) + ".jpg"
                category = Category(name=name, image_name=image_name)
                rand3 = random.randint(1, 89)
                
                for l in range(rand3):
                    product_name = rng.generate_name()[4:-5].capitalize()
                    image_name = "product-" + str(random.randint(1, 9)) + ".jpg"
                    price = random.uniform(1.0, 1000.0)
                    product = Product(name=product_name, price=price, image_name=image_name)
                    shop.products.append(product)
                    category.products.append(product)

                    product.save()
                category.save()
            shop.save()
        user.save()
                    
                    
            

if __name__ == "__main__":
    main()

    print("\n"*3)
    print("--"*4, "Everything", "--"*4)
    print("\n"*3)
    for i in storage.all().values():
        print(i)
        print("--"*10)

    print("\n"*3)
    print("--"*4, "Users", "--"*4)
    print("\n"*3)
    for i in storage.all("User").values():
        print(i)
        print("--"*10)


    print("\n"*3)
    print("--"*4, "Shops", "--"*4)
    print("\n"*3)
    for i in storage.all("Shop").values():
        print(i)
        print("--"*10)

    print("\n"*3)
    print("--"*4, "Products", "--"*4)
    print("\n"*3)
    for i in storage.all("Product").values():
        print(i)
        print("--"*10)


    print("\n"*3)
    print("--"*4, "Tags", "--"*4)
    print("\n"*3)
    for i in storage.all("Category").values():
        print(i)
        print("--"*10)
    