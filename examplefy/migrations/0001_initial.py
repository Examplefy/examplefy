# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200, null=True)),
                ('date', models.DateField()),
                ('concept', models.ForeignKey(to='examplefy.Concept')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='example',
            name='topic',
            field=models.ForeignKey(to='examplefy.Topic'),
        ),
        migrations.AddField(
            model_name='concept',
            name='topic',
            field=models.ForeignKey(to='examplefy.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='example',
            field=models.ForeignKey(to='examplefy.Example'),
        ),
    ]
