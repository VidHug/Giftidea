# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-24 09:28
from __future__ import unicode_literals

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_produit_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(blank=True, default=None, null=True, upload_to=app.models.Picture.generate_filename)),
            ],
        ),
    ]
