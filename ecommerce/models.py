from django.db import models


class Cart(models.Model):
    belongs_to = models.ForeignKey("User")
    items = models.ManyToManyField("Item")


class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    art_nr = models.IntegerField()
    price = models.DecimalField()
    sale = models.DecimalField(max_length=100)


class PackageDeal(models.Model):
    items = models.ManyToManyField("Item")
    price = models.DecimalField()

