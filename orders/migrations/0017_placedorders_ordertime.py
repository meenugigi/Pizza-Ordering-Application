# Generated by Django 3.0.6 on 2020-05-12 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_remove_placedorders_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorders',
            name='ordertime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 16, 10, 34, 670688)),
        ),
    ]