from django.contrib import admin

# Register your models here

from . import models

admin.site.register(models.Phone)
admin.site.register(models.PhoneType)
admin.site.register(models.Persone)
