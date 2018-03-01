from django.db import models


class Cart(models.Model):
    # belongs_to = models.ForeignKey("User", on_delete=None)
    items = models.ManyToManyField("Item")


class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    art_nr = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    sale = models.DecimalField(decimal_places=2, max_digits=4)

<<<<<<< HEAD
=======

class PackageDeal(models.Model):
    items = models.ManyToManyField("Item")
    price = models.DecimalField(decimal_places=2, max_digits=9)

>>>>>>> eb0d05afa23662d368c1f7e4d7de67aa486fdaab
