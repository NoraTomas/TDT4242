from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    # belongs_to = models.ForeignKey("User", on_delete=None)
    items = models.ManyToManyField("Item")


class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    art_nr = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    sale = models.DecimalField(decimal_places=2, max_digits=4)
    author = models.ForeignKey("Author", on_delete=None, default=None, blank=True)
    category = models.ManyToManyField("Category", default=None, blank=True)
    owner = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.author, self.price)


class PackageDeal(models.Model):
    name = models.CharField(max_length=250, default="default")
    items = models.ManyToManyField("Item")
    price = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return "{} {}".format(self.items, self.price)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('-last_name',)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return "{}".format(self.name)
