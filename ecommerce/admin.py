from django.contrib import admin
from .models import *

# Register your models here.
# Cart model
admin.site.register(Cart)

#change header to the Admin
admin.site.site_header = "Admin"

#item model
class ItemAdmin(admin.ModelAdmin):
    #added list view for admin
    list_display = ('name','description','art_nr','price','sale')
    #added search function for admin, search by name,price, art number, sale
    search_fields = ('name','price','art_nr','sale')
admin.site.register(Item,ItemAdmin)

#packgedeal model
class PackageDealAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    name_hierarchy = 'name'
    ordering = ('-price',)
    filter_horizontal = ('items',)
admin.site.register(PackageDeal,PackageDealAdmin)