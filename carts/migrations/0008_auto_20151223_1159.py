# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_auto_20151223_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='carts.CartItem'),
        ),
    ]
