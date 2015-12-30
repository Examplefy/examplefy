# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productfeatured_make_image_background'),
        ('carts', '0008_auto_20151223_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=1, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Variation', through='carts.CartItem2'),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.AddField(
            model_name='cartitem2',
            name='cart',
            field=models.ForeignKey(to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem2',
            name='item',
            field=models.ForeignKey(to='products.Variation'),
        ),
    ]
