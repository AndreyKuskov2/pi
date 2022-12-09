from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Menu)
admin.site.register(models.Category)