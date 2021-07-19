from django.contrib import admin
from .models import itemDetails, offerTypeAndValue, myOrder

@admin.register(itemDetails, offerTypeAndValue, myOrder)
class OrderAdmin(admin.ModelAdmin):
    pass

