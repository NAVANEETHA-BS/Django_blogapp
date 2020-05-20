# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('phno', models.CharField(max_length=20)),
                ('contact_email', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]