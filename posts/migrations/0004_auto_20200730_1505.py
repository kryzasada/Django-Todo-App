# Generated by Django 3.0.8 on 2020-07-30 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200730_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]