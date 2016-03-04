# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_auto_20160304_1809'),
        ('products', '0036_remove_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, to='answers.AnswerAccount', null=True),
        ),
    ]
