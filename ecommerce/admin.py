from django.contrib import admin
from .models import *


# Registering models here.
admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(PackageDeal)
admin.site.register(Author)
admin.site.register(Category)


# change header to the Admin
admin.site.site_header = "Admin"


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'art_nr', 'price', 'sale')


admin.site.register(Item,ItemAdmin)
