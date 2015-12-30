# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productfeatured_make_image_background'),
        ('carts', '0005_remove_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='carts.CartItem'),
        ),
    ]
