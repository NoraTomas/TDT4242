# Generated by Django 2.0.2 on 2018-03-03 16:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0002_auto_20180301_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(blank=True, default=0, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
