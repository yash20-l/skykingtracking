# Generated by Django 4.0.6 on 2022-07-19 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcode', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.datetime(2022, 7, 19, 10, 17, 34, 103430))),
            ],
        ),
    ]