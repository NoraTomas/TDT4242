# Generated by Django 2.0.2 on 2018-03-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_item_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
