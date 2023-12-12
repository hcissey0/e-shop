#!/usr/bin/python3
"""This file will populate the category table"""

from models import storage
from models.category import Category


cat_list = ['Adult', 'Antiques & Collectibles', 'Apparel', 'Arts & Entertainment', 'Attractions', 'Autos & Vehicles', 'Beauty & Fitness', 'Books & Literature', 'Business & Industrial', 'Computers', 'Consumer Electronics', 'Coupons & Discounts', 'Finance', 'Firearms & Weapons', 'Food & Drink', 'Games', 'Gifts & Special Events', 'Health', 'Holidays & Seasonal', 'Home & Garden', 'Internet', 'Jobs & Education', 'Legal Services', 'Libraries & Museums', 'Mass Merchants & Department Stores', 'People & Society', 'Pets & Animals', 'Photo & Video Services', 'Safety & Survival', 'Science', 'Smoking & Vaping', 'Sports', 'Toys & Hobbies', 'Travel', 'Wedding', 'None']

for cat in cat_list:
    category = Category(name=cat)
    category.save()