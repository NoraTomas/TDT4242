# Generated by Django 2.0.2 on 2018-04-03 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_auto_20180324_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]