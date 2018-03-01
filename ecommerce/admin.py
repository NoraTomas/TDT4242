from django.contrib import admin
from . import models

admin.site.register(models.Cart)
admin.site.register(models.Item)
admin.site.register(models.PackageDeal)
admin.site.register(models.Author)
admin.site.register(models.Category)