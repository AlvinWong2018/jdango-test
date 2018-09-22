# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('book_title', models.CharField(max_length=20)),
                ('book_pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hero_name', models.CharField(max_length=20)),
                ('hero_gender', models.BooleanField()),
                ('hero_content', models.CharField(max_length=100)),
                ('hero_book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
