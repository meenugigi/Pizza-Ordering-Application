# Generated by Django 3.0.6 on 2020-05-12 09:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_placedorders_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorders',
            name='no',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=50),
        ),
    ]
