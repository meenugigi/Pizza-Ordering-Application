# Generated by Django 3.0.6 on 2020-05-12 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_ordersplaced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordersplaced',
            old_name='created_at',
            new_name='ordertime',
        ),
    ]
