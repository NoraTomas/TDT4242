from django.contrib import admin
from .models import *


# Register your models here.

# Cart model
admin.site.register(Cart)



#change header to the Admin
admin.site.site_header = "Admin"

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','description','art_nr','price','sale')

#Item model
admin.site.register(Item,ItemAdmin)