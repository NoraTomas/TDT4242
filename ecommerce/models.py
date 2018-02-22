from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

class Cart(models.Model):
    #This class defines the Cart. Since Django does not have immediate support for Arrays/lists,
    #the idea is to have a "one-to-many" -relation from items to Cart somehow, it seems to be the Django way
    #Create fields for creation date, and if the cart is checked out or not.
    creation_date = models.DateTimeField(verbose_name=('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=('checked out'))

    #Some definitions to make it human-readable:
    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = _('-creation_date',)


