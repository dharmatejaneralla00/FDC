from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.TransitDetails)
admin.site.register(models.BookingData)
admin.site.register(models.Destinations)