from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = [
        'name',
        'price',
        'discount_price'
    ]


admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Customer)