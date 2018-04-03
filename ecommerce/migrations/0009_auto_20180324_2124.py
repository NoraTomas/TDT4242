# Generated by Django 2.0.2 on 2018-03-24 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_item_package_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='package_deal',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
    ]