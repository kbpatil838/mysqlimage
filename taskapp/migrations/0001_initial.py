# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('empname', models.CharField(max_length=100)),
                ('email', models.EmailField(error_messages={'unique': 'This Email is Already Exist.'}, unique=True, max_length=120)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'Female')], max_length=6)),
                ('status', models.CharField(max_length=7)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
